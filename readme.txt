README: Pruebas de E2E Demoblaze con Selenium

Descripción
Este proyecto automatiza pruebas de la E2E de Demoblaze utilizando Selenium. Las pruebas abarcan operaciones básicas como crear y obtener productos.

Requisitos: Antes de ejecutar las pruebas, asegúrate de tener lo siguiente:
1. Node.js instalado: Descárgalo desde [nodejs.org](https://nodejs.org/).
2. Dependencias de Selenium: Se instalan automáticamente en este proyecto.

Instalación

1. Instalar Dependencias: pip install selenium requests

2. Configuración del Entorno: Asegúrate de tener los archivos test_add_to_cart.py, test_complete_purchase.py, test_view_cart.py en la raíz del proyecto /tests.

3. Ejecutar las Pruebas: Ejecuta el script para generar el reporte html desde la terminal: python -m pytest --html=reports/api_test_report.html

4. Instalar Selenium utilizando el siguiente comando: npm install -g selenium-side-runner

5. Luego instalar la extensión de Selenium para el navegador, en este caso usamos el siguiente comando: npm install -g edgedriver

6. En el entorno de Selenium crear un proyecto denominado demoblaze

7. Hacemos clic en el icono de más en la opción Tests, y ponemos en el Test Case test1 y asi sucesivamente. Después hacemos clic en Add para añadir tarea.
   
8. A continuación procederemos a ingresar la url que nos permitirá hacer las pruebas pertinentes (https://www.demoblaze.com)

9. Luego de tener la url puesta en prueba hacemos clic en la opcion REC

10. Hacemos prueba con la url.

11. Luego de esa prueba hacemos clic en Run All Tests

12s. Si queremos cambiar algo en Selenium tanto en un front como en un back podemos cambiar los mensajes de prueba o cualquier objeto.