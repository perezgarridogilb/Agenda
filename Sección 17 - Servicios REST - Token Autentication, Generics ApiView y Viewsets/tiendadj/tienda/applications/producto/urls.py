from django.urls import include, re_path, path 

# local 
from . import views

app_name="producto_app" 

urlpatterns = [
    path('api/product/por-usuario/', 
         views.ListProductUser.as_view(), 
         name='product-producto_by_user'
         )
]
