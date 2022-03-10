from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# 
from django.views.generic import (
    ListView,
)
#
from .models import Favorites

# Esta pantalla sólo la van a poder visitar usuarios logueados 
class UserPageView(LoginRequiredMixin, ListView): 
    template_name = "favoritos/perfil.html"
    context_object_name = "entradas_user"
    login_url = reverse_lazy('users_app:user-login')
    
    def get_queryset(self):
        # Le envíamos el usuario activo en la sesión
        return Favorites.objects.entradas_user(self.request.user)