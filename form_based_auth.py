import requests
from config import SQL_EX_LOGIN, SQL_EX_PASSWORD

login_url = "https://sql-ex.ru/index.php"

session = requests.Session()


payload = {
    'login': SQL_EX_LOGIN,
    'psw': SQL_EX_PASSWORD,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/129.0.6668.90 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'ru'
}

login_response = session.post(login_url, data=payload, headers=headers)

good_login_assertion: str = 'Выход'

if login_response.ok and good_login_assertion.lower() in login_response.text.lower():
    print("Успешная авторизация")
else:
    print("Ошибка авторизации")
