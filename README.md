# Rental Scraper Full Stack App

Este proyecto es una aplicación full stack que utiliza Flask para el backend y React para el frontend. Proporciona una API para realizar scraping de listados de propiedades desde varios sitios web.

## Requisitos

- Python 3.x
- Node.js y npm
- pip (gestor de paquetes de Python)

## Instalación

### Backend (Flask)

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/rentalScraper.git
   cd rentalScraper/backend
   ```

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   - En **Windows**:

     ```bash
     source venv\Scripts\activate
     ```

   - En **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

### Frontend (React)

1. **Navega al directorio del frontend:**

   ```bash
   cd ../frontend
   ```

2. **Instala las dependencias:**

   ```bash
   npm install
   ```

## Ejecución

### Backend (Flask)

1. **Configura la variable de entorno `FLASK_APP`:**

   - En **Windows**:

     ```bash
     set FLASK_APP=app.py
     ```

   - En **macOS/Linux**:

     ```bash
     export FLASK_APP=app.py
     ```

2. **Inicia la aplicación Flask:**

   ```bash
   flask run
   ```

3. **Accede a la aplicación:**

   Abre un navegador web y ve a `http://127.0.0.1:5000/` para verificar que el servidor Flask está corriendo.

### Frontend (React)

1. **Inicia la aplicación React:**

   ```bash
   npm start
   ```

2. **Accede a la aplicación:**

   Abre un navegador web y ve a `http://localhost:3000/` para ver la aplicación React en funcionamiento.

## Uso

- **Endpoint `/`:** Verifica que el servidor Flask está corriendo.
- **Endpoint `/scrape`:** Realiza scraping de un sitio específico. Envía un JSON con el campo `site` especificando el sitio a scrapear.
- **Endpoint `/scrape_all`:** Realiza scraping de todos los sitios configurados.

## Contribuciones

Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.