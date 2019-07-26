from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('yo-viewset', views.YoViewSets, base_name="yo-viewset")
router.register('profile', views.UserProfileViewSet) #no base_name required

urlpatterns = [
    path('yo/', views.YoApiView.as_view()),
    path('', include(router.urls)),
]