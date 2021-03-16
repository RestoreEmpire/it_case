# it_case

Проект работает на Linux

Зависимости пакетов Linux:
  python3 
  mysql

Зависимости библиотек pip:
flask 
flask-sqlalchemy 
flask-migrate 
flask-login 
flask-wtf 
pymysql 
flask-bootstrap 
email_validator 
cryptography

 Установка Flask и создание виртуальной среды
https://flask.palletsprojects.com/en/1.1.x/installation/

 Чтобы подключиться к MySQL нужно изменить config.py
 
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://пользователь:пароль@имя_сервера/бд'
  
 Если использовать Sqlite:
 
 SQLALCHEMY_DATABASE_URI = 'sqlite:///директория/файл.db'
 
 В таком случае
Пакет pymysql не нужен
