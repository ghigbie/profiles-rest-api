from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('yo-viewset', views.YoViewSets, base_name="yo-viewset")
router.register('profile', views.UserProfileViewSet) #no base_name required

urlpatterns = [
    path('yo/', views.YoApiView.as_view()),
    path('', include(router.urls)),
]
