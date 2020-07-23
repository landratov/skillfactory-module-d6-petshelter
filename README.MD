**Проект: Приют домашних животных — D6**

Локальное развертывание проекта:
1. Скачиваем или клонируем репозиторий
1. Активируем виртуальное окружение
1. cd *<%путь до папки%>*
1. pip install requirements.txt
1. Необходимо установить postgresql и добавить настройки подключения к БД в settings.py вместо текущих
1. python manage.py migrate
1. python manage.py loaddata fixtures.json
1. Создаем суперюзера python manage.py createsuperuser
1. python manage.py runserver
1. Проект поднимется по адресу http://127.0.0.1:8000

Проект на хероку: https://lit-springs-28508.herokuapp.com/