import requests
import base64

username = "user"
password = "pass"

credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

url = "https://authenticationtest.com/HTTPAuth/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": f"Basic {encoded_credentials}",  # логин и пароль в Base64
    "Connection": "keep-alive",
    "Host": "authenticationtest.com",
    "Referer": "https://authenticationtest.com/",
    "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 "
                  "Safari/537.36"
}

# Используем сессию для получения куки и выполнения запросов
with requests.Session() as session:
    try:
        # Отправляем первый запрос, чтобы получить куки
        response = session.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("Авторизация прошла успешно!")
            print("Полученные куки:", session.cookies.get_dict())
        elif response.status_code == 401:
            print("Ошибка авторизации: неверный логин или пароль (401 Unauthorized)")
        elif response.status_code == 403:
            print("Доступ запрещен (403 Forbidden)")
        elif response.status_code >= 500:
            print(f"Ошибка на стороне сервера (код {response.status_code})")
        else:
            print(f"Неизвестная ошибка: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания запроса (timeout)")
    except requests.exceptions.ConnectionError:
        print("Ошибка: Не удалось подключиться к серверу (connection error)")
    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}")
    except Exception as err:
        print(f"Произошла непредвиденная ошибка: {err}")
