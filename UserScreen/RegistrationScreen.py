import tkinter as tk
from tkinter import messagebox

import os
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from ServerAPI.Requast import ServerClient
from ViewModel.UserViewModel import UserViewModel


class RegistrationScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.user_view_model = UserViewModel(ServerClient("https://meetmap.up.railway.app"))  # Инициализация
        self.data_directory = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data"  # Путь к директории
        self.uid_file = os.path.join(self.data_directory, "uid.txt")  # Путь к файлу UID
        self.create_widgets()

    def create_widgets(self):
        # Метки и поля ввода
        tk.Label(self, text="Имя:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Пароль:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Пол:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.gender_var = tk.StringVar(value="male")
        gender_menu = tk.OptionMenu(self, self.gender_var, "male", "female", "other")
        gender_menu.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Возраст:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=4, column=1, padx=10, pady=5)

        # Кнопка для отправки данных (регистрация)
        submit_button = tk.Button(self, text="Регистрация", command=self.submit)
        submit_button.grid(row=5, columnspan=2, pady=10)

        # Кнопка для перехода на экран входа
        login_button = tk.Button(self, text="Войти", command=self.go_to_login)
        login_button.grid(row=6, columnspan=2, pady=10)

    def submit(self):
        # Получаем данные из полей ввода
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        gender = self.gender_var.get()
        age = self.entry_age.get()

        # Проверка на корректность ввода
        if not name or not email or not password or not gender or not age:
            messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
            return

        # Вызов метода для регистрации
        self.user_view_model.create_user(
            name, email, password, gender, age, self.handle_registration_result
        )

    def handle_registration_result(self, result):
        """Обрабатывает результат регистрации."""
        if isinstance(result, dict) and result.get("status") is True and "uid" in result:
            uid = result["uid"]
            self.save_uid(uid)  # Сохраняем UID
            messagebox.showinfo("Успех", f"Регистрация завершена! UID: {uid}")
            self.controller.show_screen("login")  # Переход на экран входа
        else:
            messagebox.showerror("Ошибка", "Не удалось зарегистрироваться. Проверьте данные!")

    def save_uid(self, uid):
        """Сохраняет UID в файл."""
        try:
            os.makedirs(self.data_directory, exist_ok=True)  # Создаем директорию, если её нет
            with open(self.uid_file, 'w') as file:
                file.write(uid)  # Перезаписываем UID
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить UID: {e}")

    def go_to_login(self):
        """Метод для перехода на экран входа."""
        from UserScreen.LoginScreen import LoginScreen  # Отложенный импорт
        self.destroy()  # Удаляем текущий экран
        login_screen = LoginScreen(self.root, self.controller)
        login_screen.pack(expand=True, fill="both")
