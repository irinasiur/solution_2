import os
from dotenv import load_dotenv

load_dotenv()

SQL_EX_LOGIN = os.getenv('SQL_EX_LOGIN')
SQL_EX_PASSWORD = os.getenv('SQL_EX_PASSWORD')

if not SQL_EX_LOGIN or not SQL_EX_PASSWORD:
    raise ValueError("Логин или пароль не найдены в файле .env")
