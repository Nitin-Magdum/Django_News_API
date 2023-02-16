from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
key = '87a3ed8b47ef4ac38e1f65d2110d6562'


class NewsView(APIView):
    def get(self, request):
        category = request.GET.get('category')
        page = request.GET.get('page')
        page_size = request.GET.get('page_size')

        if not category:
            return Response({'error': 'Please provide a category'}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={key}"
        if page:
            url += f"&page={page}"
        if page_size:
            url += f"&pageSize={page_size}"
      
        response = requests.get(url)
        if response.status_code == status.HTTP_200_OK:
            return Response(response.json())
        else:
            return Response({'error': 'Unable to retrieve news'}, status=status.HTTP_400_BAD_REQUEST)
