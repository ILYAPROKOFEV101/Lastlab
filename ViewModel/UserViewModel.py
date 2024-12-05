from threading import Thread


class UserViewModel:
    def __init__(self, server_client):
        self.server_client = server_client
        self.is_loading = False

    def create_user(self, name, email, password, gender, age, callback):
        """Создание пользователя и обработка результата."""
        self.is_loading = True
        # Создаем новый поток для выполнения запроса
        thread = Thread(target=self._create_user_thread, args=(name, email, password, gender, age, callback))
        thread.start()

    def _create_user_thread(self, name, email, password, gender, age, callback):
        """Выполнение запроса на создание пользователя в отдельном потоке."""
        result = self.server_client.great_user(name, email, password, gender, age)
        # После завершения запроса, вызываем callback
        callback(result)

    def login(self, email, password, callback):
        """Авторизация пользователя и обработка результата."""
        self.is_loading = True
        thread = Thread(target=self._login_thread, args=(email, password, callback))
        thread.start()

    def _login_thread(self, email, password, callback):
        """Выполнение запроса на получение UID пользователя в отдельном потоке."""
        result = self.server_client.get_uid(email, password)
        # После завершения запроса, вызываем callback
        callback(result)