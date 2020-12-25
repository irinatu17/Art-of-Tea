from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/', views.contact_thankyou, name='contact_thankyou'),
]
