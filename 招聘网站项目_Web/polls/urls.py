from os import name
from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_main_page),
    path('wordcloud/', views.show_wordcloud),
    path('form/', views.show_form),
    path('salary/', views.show_salary),
    path('test/', views.test),
    path('search/', views.search_button),
    path('craw/', views.craw),
]
