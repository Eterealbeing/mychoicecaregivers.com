from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def donate(request):
    return render(request, 'donate.html')


def news(request):
    return render(request, 'news.html')


def news_details(request):
    return render(request, 'news-detail.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def volunteer(request):
    return render(request, 'volunteer.html')
