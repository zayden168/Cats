from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

# def cats(request):
#     return render(request, 'main/СatsGallery.html')

# def profile(request):
#     return render(request, 'main/profile.html')