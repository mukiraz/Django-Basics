from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('details/', views.details, name = 'details'),
    path('<int:category_id>', views.getProductsByCategoryID, name = "categoryId"),
    path('<str:category>', views.getProductsByCategory, name = 'products_by_category')
    
]