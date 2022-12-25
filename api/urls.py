from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Products'), # viewing all product
    path('createproduct', views.createProduct, name='Create Product'), # creating new product 
    path('<str:pk>/delete', views.deleteProduct, name="Delete Product"), # deleting a product
    path('<str:pk>', views.readProduct, name='Update Product'), # viewing a product
]