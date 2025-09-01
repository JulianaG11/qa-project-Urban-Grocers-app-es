 SPRINT 7      Proyecto Urban Grocers      Cohorte 36
En este proyecto estuve trabajando con una lista de comprobación para el campo "name" en la solicitud de creación de un kit de productos, estas pruebas se realizaron basadas en la información que contenia  API DOC de Urban Gorcers, en la sección de creación de kits; se creo un kit y un usuario para cada prueba, los resultados fueron diferentes en cada prueba pero los pasos basicamente fueron los mismos, modificando el kit body en el archivo data, de acuerdoa lo que pedian en la lista de comprbación y basado en la API DOC.
Se realizaron 9 pruebas automatizadas desde la lista de comprobaci�n de las cuales 4 salieron No aprobadas y 5 salieron Aprobadas, en el siguiente orden:

Prueba 1: Aprobada, ambos resultados, tanto el esperado como el resultado actual código 201.
Prueba 2: Aprobada, ambos resultados código 201.
Prueba 3: No Aprobada ya que el resultado esperado era código 400 y el resultado actual fue código 201.
prueba 4: No Aprobada, resultado esperado código 400 y el resultado actual fue código 201.
Prueba 5: Aprobada, ambos resultados código 201.
Prueba 6: Aprobada, ambos resultados código 201.
Prueba 7: Aprobada, ambos resultados código 201.
Prueba 8: No Aprobada, resultado esperado código 400 y resultado actual código 500.
Prueba 9: No Aprobada, resultado esperado código 400 y rsultado actual código 201.
Se crearon 6 archivos en el proyecto para realizar las pruebas:
configutation.py: configuración del servidor/URLs.
data.py: datos de prueba ( nombre del kit etc).
create_kit_name_kit_test.py: archivo principal para hacer las pruebas.
sender_stand_request.py: funciones para enviar request HTTP.
README.md: explicación del proyecto.
gitignore: aqui van archivos innecesarios del repositorio.
Métodos y técnicas utilizadas: método GET y POST, lenguaje Python, biblioteca request HTTP, Pytest.


 
