
from django.urls import path, include
from rest_framework import routers
from senapi import views # type: ignore

router = routers.DefaultRouter()
router.register(r'senapi', views.ApisenaView, 'senapi')
urlpatterns = [
    path("api/v1/", include (router.urls))
]