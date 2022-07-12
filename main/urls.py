from django.contrib import admin
from django.urls import path 
from .views import HomePageView , AboutView , NewsView , ContactView , cange_lane


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('news/',NewsView.as_view(),name = 'news'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('cange_lane',cange_lane,name='cange_lane'),

]