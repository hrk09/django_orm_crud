from django.urls import path
from . import views

# articles/ 이후의 경로가 들어오면 됨!
urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),

]