from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    # we send category id as a parameter
    path('<int:category_id>', views.getProductsByCategoryID, name = "categoryId"),
    # we send category as a parameter
    path('<str:category>', views.getProductsByCategory, name = 'products_by_category')
    
]