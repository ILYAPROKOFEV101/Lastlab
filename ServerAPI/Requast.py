import requests


class ServerClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def great_user(self, name, email, password, gender, age):
        """Отправляет POST-запрос на создание пользователя."""
        url = f"{self.base_url}/greatUser"
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "gender": gender,
            "age": age
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response.json()  # Возвращаем JSON-ответ от сервера
        except requests.RequestException as e:
            return f"Ошибка при отправке запроса: {e}"

    def get_uid(self, email, password):
        """Отправляет POST-запрос для получения UID пользователя."""
        url = f"{self.base_url}/getUid"
        payload = {
            "email": email,
            "password": password
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response.json()  # Возвращаем JSON-ответ от сервера
        except requests.RequestException as e:
            return f"Ошибка при отправке запроса: {e}"


