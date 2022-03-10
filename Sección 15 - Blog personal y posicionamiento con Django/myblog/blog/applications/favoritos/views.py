from ast import Delete
from http.client import HTTPResponse 
# 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# 
from django.views.generic import ( 
    DeleteView,                              
    View,
    ListView,
)
#
from applications.entrada.models import Entry
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

# En este caso no nos sirve CreateView o ListView    
class AddFavoritosView(LoginRequiredMixin, View): 
    login_url = reverse_lazy('users_app:user-login')
    # Sin ningún template o nada ejecutar el método post 
    def post(self, request, *args, **kwargs): 
        # Recuperar el usuario 
        usuario = self.request.user 
        entrada = Entry.objects.get(id=self.kwargs['pk']) 
        # Registramos favorito 
        Favorites.objects.create( 
            user=usuario, 
            entry=entrada,
        ) 
        
        return HttpResponseRedirect( 
            reverse(
                'favoritos_app:perfil'
                )
        )
        
class FavoritesDeleteView(DeleteView):
    model = Favorites 
    success_url = reverse_lazy('favoritos_app:perfil')
        