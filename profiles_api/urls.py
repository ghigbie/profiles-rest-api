from django.urls import path
from profiles_api import views

urlpatterns = [
    path('yo/', views.YoApiView.as_view())
]