# Backend para Irakani App Generator

Este servidor Express actúa como proxy para las llamadas a la API de Irakani y maneja las operaciones de AWS.

## Configuración

1. Instala las dependencias:
   ```
   npm install
   ```

2. Crea un archivo `.env` basado en `.env.example` y configura tus credenciales AWS:
   ```
   PORT=5000
   AWS_REGION=us-east-1
   AWS_ACCESS_KEY_ID=tu_access_key_aqui
   AWS_SECRET_ACCESS_KEY=tu_secret_key_aqui
   AWS_SESSION_TOKEN=tu_session_token_aqui_si_es_necesario
   ```

3. Inicia el servidor:
   ```
   npm start
   ```

   O en modo desarrollo:
   ```
   npm run dev
   ```

## Endpoints

- `POST /api/analyze`: Proxy para el endpoint de análisis
- `POST /api/generate`: Proxy para el endpoint de generación
- `POST /api/stepfunctions/status`: Consulta el estado de una ejecución de Step Functions
- `POST /api/s3/download`: Descarga un archivo desde S3# star-wars-test
