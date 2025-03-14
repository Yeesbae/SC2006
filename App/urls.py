# Description: This file contains the URL patterns for the app.

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
    path('api/create-entry/', views.create_entry, name='create_entry'),
    path('api/add-entry/', views.add_entry, name='add_entry'),
    path('api/update-entry/', views.update_entry, name='update_entry'),
    path('api/delete-entry/', views.delete_entry, name='delete_entry'),
    # path('api/get-input/', views.get_input, name='get_input'),
    path('api/delete-latest/', views.delete_latest_entry, name='delete_latest_entry'),
    path('api/delete-all/', views.delete_all_entry, name='delete_all_entry'),
    path('api/get-entry/', views.get_entry, name='get_entry'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()