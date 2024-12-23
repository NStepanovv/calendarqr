# calendarqr

## Запуск приложения на удаленном сервере
1. Обновление apt и установка git

sudo apt update
sudo apt install git

2. Установка Docker и docker-compose

https://totaku.ru/ustanovka-docker-i-docker-compose-na-ubuntu-24-04/

3. Установка репозитория

git clone ...

4. Установить IP и домен в качестве ALLOWED_HOSTS и заменить логин, пароль для БД

cd backend cp .env.example .env
vi .env

cd infra cp .env.example .env
vi .env

5. Запуск приложения

docker compose up -d

6. Создание суперпользователя

docker exec -it django_backend python manage.py cratesuperuser