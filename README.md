# it_case

Зависимости:
  python3 
  бд(используется mysql)

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

 Чтобы подключиться к MySQL(или другой бд) нужно изменить config.py
 
MySQL:
 
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://пользователь:пароль@имя_сервера/бд'
  
Sqlite:
 
 SQLALCHEMY_DATABASE_URI = 'sqlite:///директория/файл.db'
 
 В таком случае
Пакет pymysql не нужен
