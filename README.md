Descripción del programa
Este programa demuestra el uso de constructores (`__init__`) y destructores (`__del__`) en Python.
Se modela un objeto `Archivo` que abre un archivo al crearse y libera el recurso al eliminarse.
La lógica de escritura se gestiona mediante una clase de servicio.

Cómo ejecutar el programa
1. Asegúrese de tener Python instalado.
2. Ejecute el archivo principal con el comando:
   ```
   python main.py
   ```
3. El programa creará un archivo de texto y mostrará mensajes en consola.
   
Uso de __init__ y __del__
- `__init__`: se ejecuta al crear el objeto `Archivo`, inicializando atributos y abriendo el archivo.
- `__del__`: se ejecuta cuando el objeto se elimina o finaliza el programa, cerrando el archivo y liberando el recurso.
