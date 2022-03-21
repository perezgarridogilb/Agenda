from django.urls import include, re_path, path 

# local 
from . import views

app_name="producto_app" 

urlpatterns = [
    path('api/product/por-usuario/', 
         views.ListProductUser.as_view(), 
         name='product-producto_by_user'
         ), 
    path('api/product/con-stok/', 
         views.ListProductStok.as_view(), 
         name='product-producto_con_stok'
         ), 
    # Lista de productos por genéros
    path('api/product/pon-genero/<gender>/', 
         views.ListProductGenero.as_view(), 
         name='product-producto_pon_genero'
    ), 
    path('api/product/filtrar/', 
         views.FiltrarProductos.as_view(), 
         name='product-filtrar'
    ) 
]
