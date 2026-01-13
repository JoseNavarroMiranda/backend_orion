# Backend Orion

Backend desarrollado con Django para el proyecto Orion.

## Requisitos Previos

- Docker
- Docker Compose
- Archivo `.env` configurado con las variables de entorno necesarias

## Comandos de Docker Compose

### Levantar los contenedores (Desarrollo)

**Importante**: Antes de levantar los contenedores en modo desarrollo, es necesario crear la red Docker manualmente porque el archivo `docker-compose.yml` la define como red externa (`external: true`):

```bash
docker network create backend-net
```

Nota: En el modo producción (`docker-compose.prod.yml`), la red se crea automáticamente porque usa `driver: bridge`.

Para iniciar los contenedores en modo desarrollo:

```bash
docker-compose up
```

O para ejecutarlo en segundo plano (detached mode):

```bash
docker-compose up -d
```

### Levantar los contenedores (Producción)

Para iniciar los contenedores en modo producción:

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Detener los contenedores

```bash
docker-compose down
```

Para producción:

```bash
docker-compose -f docker-compose.prod.yml down
```

### Ver los logs de los contenedores

Ver todos los logs:

```bash
docker-compose logs
```

Ver logs en tiempo real:

```bash
docker-compose logs -f
```

Ver logs de un servicio específico:

```bash
docker-compose logs -f web
docker-compose logs -f db
```

### Reconstruir los contenedores

Si has hecho cambios en el Dockerfile o en las dependencias:

```bash
docker-compose build
docker-compose up -d
```

O en un solo comando:

```bash
docker-compose up -d --build
```

### Otros comandos útiles

Listar los contenedores en ejecución:

```bash
docker-compose ps
```

Ejecutar comandos dentro del contenedor web:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic
```

Acceder a la shell del contenedor:

```bash
docker-compose exec web bash
```

Acceder a la base de datos MySQL:

```bash
docker-compose exec db mysql -u ${MYSQL_USER} -p ${MYSQL_DATABASE}
```

Nota: El comando solicitará la contraseña de forma interactiva por seguridad.

## Configuración del archivo .env

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# MySQL Configuration
MYSQL_ROOT_PASSWORD=CHANGE_ME_secure_root_password
MYSQL_DATABASE=orion_db
MYSQL_USER=orion_user
MYSQL_PASSWORD=CHANGE_ME_secure_password
MYSQL_HOST=db
MYSQL_PORT=3306
```

**Importante**: Cambia los valores `CHANGE_ME` por contraseñas seguras antes de usar en producción.

## Acceso a la aplicación

Una vez levantados los contenedores, la aplicación estará disponible en:

```
http://localhost:8000
```

## Arquitectura

El proyecto utiliza dos servicios principales:

- **web**: Aplicación Django corriendo en el puerto 8000
- **db**: Base de datos MySQL 8.0 corriendo en el puerto 3306

Ambos servicios están conectados a través de una red Docker llamada `backend-net`.
