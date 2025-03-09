# Description: This file contains the URL patterns for the app.

# from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', views.main, name='main'),
    path('api/', include(router.urls)),
    path('api/account/', views.get_account, name='get_account'),
    path('api/account/create/', views.create_account, name='create_account'),
    path('api/save/', views.create_user, name='create_user'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()