# Как установить

## Установка виртуального окружения и зависимостей:  
python -m venv venv  
.\venv\Scripts\activate  
cd .\diplom\  
pip install -r requirements.txt

## База данных
Создать бд
Поменять строку подключения в settings.py
python manage.py migrate

Запуск сервера:  
python manage.py runserver  
