Клонировать репозиторий: git clone https://github.com/yourusername/abcd123.git;  cd abcd123
Создать виртуальное окружение: python3 -m venv env;  source env/bin/activate
Установить зависимости: pip install -r requirements.txt
Создать базу данных PostgreSQL и добавить в settings.py
Применить миграции: python manage.py migrate
Запустить сервер: python manage.py runserver
