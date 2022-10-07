from django.urls import path

from center.views import index, contact, services, features

urlpatterns = [
    path('', index, name='index'),
    path('services', services, name='services'),
    path('features/<int:id>', features, name='features'),
    path('contact/', contact, name='contact'),
]
