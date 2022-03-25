# tiendadj
Proyecto Django para la sección de servicios Rest DRF en curso profesional 

Accediendo al token de firebase para iniciar sesión
``` 
sudo pip3 install firebase-admin 
``` 
En caso de error
``` 
sudo apt-get install python3-dev
``` 
# Login

``` 
http://localhost:8000/login/
``` 

## Axios 
Si se quiere crear una sesión, se le pasa a a la función login el usuario y "todo seguiría funcionando igual".

<img width="1392" alt="Axios" src="https://user-images.githubusercontent.com/56992179/158735000-792261bf-622f-44ba-8827-e008dd536419.png">


## Database Backup Commands 
Creando respaldo
``` 
python manage.py dumpdata --exclude auth.permission > nombre_copia_bd.json
``` 

Leyendo información de respaldo
``` 
python manage.py loaddata tienda_data.json
``` 
## Multiple parameters from URL
Ejemplo

``` 
http://127.0.0.1:8000/api/product/filtrar/?man=False&woman=True&name=a
``` 

<img width="1392" alt="Captura de Pantalla 2022-03-21 a la(s) 2 49 19 a m" src="https://user-images.githubusercontent.com/56992179/159229240-76a279d7-2e30-4409-8e2b-3d235f51f9a4.png">

## Validated_data 
Validando data de ventas

### Body 
Estructura del body raw/JSON
``` 
{
"type_invoce": "0",
"type_payment": "0",
"adreese_send": "DirB3",
"productos": []
}

``` 
### Token
<img width="1392" alt="Captura de Pantalla 2022-03-23 a la(s) 8 59 11 p m" src="https://user-images.githubusercontent.com/56992179/159833302-337786c2-a67e-45b9-a409-c4efdf71359c.png">


### POST
<img width="1392" alt="Captura de Pantalla 2022-03-23 a la(s) 8 56 35 p m" src="https://user-images.githubusercontent.com/56992179/159833190-1546f761-a290-4969-af9d-fd93e3abaf6e.png">

``` 
{
"type_invoce": "1",
"type_payment": "0",
"adreese_send": "DirB2",
"productos": [{"pk": 1,"count": 2}, {"pk": 3, "count": 1}]
}

``` 
