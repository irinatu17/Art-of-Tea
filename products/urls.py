from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>', views.service_details,
         name='service_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('services/edit/<int:service_id>/', views.edit_service,
         name='edit_service'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('services/delete/<int:service_id>/', views.delete_service,
         name='delete_service'),
    path('services/remove/<item_id>/', views.remove_itinerary_item,
         name='remove_itinerary_item'),

]
