from django.urls import path
from MyApp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('donate/', views.donate, name='donate'),
    path('news/', views.news, name='news'),
    path('news-detail/', views.news_details, name='news-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer')




]
