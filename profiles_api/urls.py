from django.urls import path, include
from profiles_api import views
from rest_framework.router import DefaultRouter

router = DefaultRouter()
router.register('yo-viewset', views.YoViewSets, base_name="yo-viewset")

urlpatterns = [
    path('yo/', views.YoApiView.as_view())
    path('', include(router.urls)
]