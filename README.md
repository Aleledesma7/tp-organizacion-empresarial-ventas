# TP Organización Empresarial - Célula de Desarrollo (Escenario B)

Buenas! Este es el repositorio central para el Trabajo Práctico de Gestión Colaborativa y Control de Versiones de la materia Organización Empresarial (Año Lectivo 2026). 

Como me tocó encarar el proyecto de manera individual, estoy simulando el flujo completo de la célula ágil y dividiendo las tareas en los tres roles pedidos por la cátedra (Hugo, Paco y Luis) para cumplir con la gobernanza y el seguimiento en Jira.

## Roles y "Equipo"
* **Líder y Organizador (Hugo):** Armado de la estructura, gobernanza del repo y documentación inicial.
* **Desarrollador Técnico (Paco):** Creación de ramas, código en Python (Google Colab) y procesamiento de los datos de ventas.
* **Revisor y QA (Luis):** Control de calidad, comentarios técnicos, gestión del .gitignore y cierre de Pull Requests.

## 📊 Escenario Elegido: Análisis de Ventas
Elegimos el Escenario B. La idea del script es importar un dataset simulado de ventas comerciales diarias para procesarlo en Python y sacar tres métricas clave:
1. Ventas totales de la empresa.
2. Identificar cuál fue el producto más vendido.
3. Calcular las ventas distribuidas por mes.

Además, el script genera un gráfico de línea para ver cómo evolucionaron las ventas a lo largo del tiempo.

## Estructura del Proyecto
El repositorio está ordenado siguiendo las buenas prácticas de la cátedra:
* `/datos`: Carpeta donde se guarda el archivo fuente (`dataset.csv`).
* `/scripts`: El código en Python (`analisis_datos.py`) con la lógica del análisis.
* `/resultados`: Los reportes generados y el gráfico final exportado en PNG.

## Cómo correr el análisis
1. Clonar este repositorio público.
2. Asegurarse de tener el archivo de las ventas dentro de la carpeta `/datos`.
3. Abrir el script de la carpeta `/scripts` en Google Colab y correr las celdas de corrido (está todo configurado con rutas relativas para que no falle).
