# Agenda
Django REST Framework Section

# REST services
Es como el puente para que se comuniquen dos software completamente independientes.

- Principalmente trabajan con archivos de formato JSON que luego va a tomar una aplicación para interpretarla, para transformarla en Objetos o Clases, que luego van a procesar para interactuar con nuestra Base de Datos.

Clave - valor
```
{
  "departamento":8,
  "nombredepto":"Ventas",
  "director": "Juan Rodríguez",
  "empleados":[
    {
      "nombre":"Pedro",
      "apellido":"Fernández"
    },{
      "nombre":"Jacinto",
      "apellido":"Benavente"
    } 
  ]
}
```
# REST Architecture
Es una interfaz para conectar sistemas basados en el protocolo HTTP
Recuperar información sobre el recurso

## Methods
GET: Recuperar información sobre el recurso API REST
POST: Crear un recurso de API REST
PUT: Actualizar un recurso de API REST
DELETE: Eliminar un recurso de la API REST o un componente relacionado

## Client - Server
Este nos obliga a tener separado lo que es del cliente y el servidor
- Todo proceso que interactúa con los datos tiene que ser un proceso exclusivamente del servidor
- Toda la interfaz grácfica con la que interactúa el usuario es del lado del cliente


