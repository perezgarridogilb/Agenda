# django
from django.urls import path

# local
from . import views

app_name="users_app"

urlpatterns = [
    # template login
    path(
        'login/', 
        views.LoginUser.as_view(), 
        name='login'
    )
]
