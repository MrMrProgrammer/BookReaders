from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'SiteSetting/index-page.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'SiteSetting/home-page.html')

    else:
        return redirect('index')
