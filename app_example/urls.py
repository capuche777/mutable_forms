from django.urls import path

from app_example.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
