from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.votedetails, name='details'),
    path('vote/<int:id>/', views.vote, name='vote'),
    path('voted/', views.voted, name='voted'),
]
