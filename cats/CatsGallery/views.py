from django.shortcuts import render
from django.http import JsonResponse
import requests

API_KEY = 'live_YbZE6XigqmoRVq0jCeq9om6mJvmQ5uLfnrKQvpxoKbLOfuHgO6whJPSpkXmqwSha'

def CatsGallery(request):
    return render(request, 'CatsGallery.html')

def CatsGalleryAPI(request):
    url = 'https://api.thecatapi.com/v1/images/search'
    params = {'limit': 28}
    headers = {'x-api-key': API_KEY}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        cat_images = response.json()
    else:
        print('Ошибка при получении изображений:', response.status_code, response.text)
        cat_images = []

    return JsonResponse(cat_images, safe=False)
