
# 💸 Gestor de Gastos

Una aplicación móvil y API backend para gestionar y controlar tus gastos diarios. Construido con **Flask** para el backend y **React Native (Expo)** para el frontend.

---

## 🚀 Tecnologías usadas

- 🐍 **Backend (Flask)**
  - Python 3
  - Flask + SQLAlchemy
  - PostgreSQL (base de datos)
  - CORS habilitado para conexión con frontend

- 📱 **Frontend (React Native con Expo)**
  - React Native
  - Expo CLI
  - Axios para llamadas HTTP
  - @react-native-picker/picker

---

## 🗂️ Estructura del proyecto

GestorDeGastos/
├── backend/ <-- API Flask
│ ├── app.py
│ ├── models.py
│ ├── config.py
│ ├── requirements.txt
│ └── ...
├── frontend/ <-- App móvil React Native
│ ├── App.js
│ ├── components/
│ ├── services/api.js
│ ├── package.json
│ └── ...
├── README.md <-- Este archivo



---

## ⚙️ Configuración del proyecto

### 🐍 Backend (Flask)

1. Clona el repositorio:
   ```bash
   git clone https://github.com/<TU_USUARIO>/gestor-gastos.git
   cd gestor-gastos/backend
Crea y activa un entorno virtual:

bash

python -m venv venv
venv\Scripts\activate   # En Windows
source venv/bin/activate # En Linux/Mac
Instala las dependencias:

bash

pip install -r requirements.txt
Configura la base de datos PostgreSQL en config.py:

python

SQLALCHEMY_DATABASE_URI = "postgresql://gestor_user:123456@localhost:5432/gestor_gastos"
Crea las tablas:

bash

python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
Ejecuta el servidor:

bash

python app.py
📍 Por defecto, el backend se ejecuta en http://<TU_IP>:5000.

📱 Frontend (React Native con Expo)
En otra terminal:

bash

cd ../frontend
Instala las dependencias:

bash

npm install
Configura la IP del backend en services/api.js:

javascript

const IP_BACKEND = "http://<TU_IP>:5000";
Inicia la app:

bash

npx expo start
Escanea el código QR con la app Expo Go en tu teléfono para probar.