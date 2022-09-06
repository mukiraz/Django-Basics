from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('index', views.index),
    path('<slug:slug>', views.details, name="product_details"),
    path('<int:category_id>', views.getProductsByCategoryId),
    path('<str:category>', views.getProductsByCategory, name='products_by_category')
    
]