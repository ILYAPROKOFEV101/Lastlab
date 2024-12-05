
import tkinter as tk
from tkinter import messagebox

from ServerAPI.Requast import ServerClient
from UserScreen.RegistrationScreen import RegistrationScreen
from ViewModel.UserViewModel import UserViewModel


class LoginScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.user_view_model = UserViewModel(
            ServerClient("https://meetmap.up.railway.app"))  # Пример создания объекта UserViewModel
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Email:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Пароль:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(self, text="Войти", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)

        back_button = tk.Button(self, text="Назад к регистрации", command=self.go_to_registration)
        back_button.grid(row=3, columnspan=2, pady=10)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Вызов метода для авторизации, передаем callback для обработки результата
        self.user_view_model.login(email, password, self.handle_login_result)

    def handle_login_result(self, result):
        """Обрабатывает результат авторизации."""
        if isinstance(result, dict) and result.get('status') is True and 'uid' in result:
            # Успешный вход
            uid = result['uid']  # Получаем UID
            messagebox.showinfo("Успех", f"Вход выполнен успешно! UID: {uid}")
            self.controller.show_screen("main")  # Переход на главный экран
        else:
            # Ошибка при авторизации
            messagebox.showerror("Ошибка", "Неправильный Email или пароль!")

    def go_to_registration(self):
        """Метод для перехода на экран регистрации."""
        from UserScreen.RegistrationScreen import RegistrationScreen  # Corrected import
        self.destroy()  # Удаляем текущий экран
        RegistrationScreen(self.root, self.controller).pack(expand=True, fill="both")
