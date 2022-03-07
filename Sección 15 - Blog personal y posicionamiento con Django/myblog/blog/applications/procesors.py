# importando el modelo home
from applications.home.models import Home

# Procesor para recuperar teléfono y correo del registro home 

# Agregado dentro de context procesor dentro de la configuración

def home_contact(request):
    home = Home.objects.latest('created') 
    # Siempre retornar como este diccionario de aquí
    return {
        'phone': home.phone,
        'correo': home.contact_email, 
        }