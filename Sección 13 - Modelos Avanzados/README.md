# Avanced Models
Django REST Framework Section

# Managers
Son una consulta a la base de datos usando buenas prácticas

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
