from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApiResponseSerializer

def get_characters_from_api():
    response = requests.get('http://localhost:5005/api/rickandmorty/characters')
    if response.status_code == 200:
        return response.json()
    else:
        return None

class CharacterListView(APIView):
    def get(self, request):
        api_response = get_characters_from_api()
        if api_response:
            serializer = ApiResponseSerializer(api_response)
            return Response(serializer.data)
        else:
            return Response({"error": "Unable to fetch data from the API"}, status=500)
