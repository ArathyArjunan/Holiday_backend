from holiday_project import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class FetchHolidaysView(APIView):
    def get(self, request):
        country = request.query_params.get('country')
        year = request.query_params.get('year')

        if not country or not year:
            return Response({"error": "Country and year are required."}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = f"holidays_{country}_{year}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        url = f"{settings.CALENDARIFIC_BASE_URL}/holidays"
        params = {
            'api_key': settings.CALENDARIFIC_API_KEY,
            'country': country,
            'year': year,
        }

        try:
            response = requests.get(url, params=params)
            response_data = response.json()

            if response.status_code == 200 and response_data.get('meta', {}).get('code') == 200:
                cache.set(cache_key, response_data['response']['holidays'], timeout=86400)
                return Response(response_data['response']['holidays'], status=status.HTTP_200_OK)
            else:
                return Response(response_data, status=response.status_code)
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



