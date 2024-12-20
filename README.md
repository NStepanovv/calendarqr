# calendarqr

## Запуск приложения на удаленном сервере
1. Обновление apt и установка git
'''
sudo apt update
sudo apt install git
'''

2. Установка Docker и docker-compose
https://totaku.ru/ustanovka-docker-i-docker-compose-na-ubuntu-24-04/

3. Установка репозитория
git clone ...

4. 









1. Временный переход на SQLite
Чтобы выполнить миграции и продолжить разработку без PostgreSQL, временно используйте SQLite в файле settings.py. Это позволит вам запускать makemigrations и migrate.

Временно замените блок DATABASES в backend/settings.py:
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

python manage.py makemigrations
python manage.py migrate

2. Настройка PostgreSQL в Docker (docker-compose.yml)
Добавьте docker-compose.yml для будущего запуска базы данных PostgreSQL и самого Django.

Пример docker-compose.yml:
version: '3.9'

services:
  db:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: calendarqr
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: django_backend
    restart: always
    environment:
      POSTGRES_DB: calendarqr
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
    volumes:
      - ./backend:/usr/src/app
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:


Понял. Если база данных еще не создана и вы планируете запускать её в Docker через docker-compose, ошибка возникает потому, что Django сейчас не может подключиться к базе данных PostgreSQL.

Шаги для решения проблемы
1. Временный переход на SQLite
Чтобы выполнить миграции и продолжить разработку без PostgreSQL, временно используйте SQLite в файле settings.py. Это позволит вам запускать makemigrations и migrate.

Временно замените блок DATABASES в backend/settings.py:

python
Копировать код
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
Теперь выполните команды:

bash
Копировать код
python manage.py makemigrations
python manage.py migrate
2. Настройка PostgreSQL в Docker (docker-compose.yml)
Добавьте docker-compose.yml для будущего запуска базы данных PostgreSQL и самого Django.

Пример docker-compose.yml:

yaml
Копировать код
version: '3.9'

services:
  db:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: calendarqr
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: django_backend
    restart: always
    environment:
      POSTGRES_DB: calendarqr
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
    volumes:
      - ./backend:/usr/src/app
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:

3. Подготовка Dockerfile для Django

4. Возврат к PostgreSQL
После запуска docker-compose, переключите settings.py обратно на PostgreSQL:
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

5. Запуск проекта
Запустите docker-compose командой:
docker-compose up --build

После этого база данных PostgreSQL будет доступна, и вы сможете снова выполнить миграции:
docker exec -it django_backend python manage.py makemigrations
docker exec -it django_backend python manage.py migrate