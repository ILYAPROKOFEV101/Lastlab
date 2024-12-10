import os
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from ServerAPI.Requast import ServerClient
from ViewModel.UserViewModel import UserViewModel


import tkinter as tk
from tkinter import messagebox, font as tkfont
import os

import tkinter as tk
from tkinter import messagebox, font as tkfont
import os

class LoginScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.user_view_model = UserViewModel(
            ServerClient("https://meetmap.up.railway.app"))
        self.data_directory = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data"
        self.uid_file = os.path.join(self.data_directory, "uid.txt")
        self.create_widgets()

    def create_widgets(self):
        # Настройка шрифтов и цветов
        title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        label_font = tkfont.Font(family="Helvetica", size=14)
        button_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        self.configure(bg="white")  # Белый фон

        # Email
        tk.Label(self, text="Email:", font=label_font, bg="white", fg="black").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.entry_email = tk.Entry(self, font=label_font, bd=2, relief="solid", width=30)
        self.entry_email.grid(row=0, column=1, padx=20, pady=10)

        # Пароль
        tk.Label(self, text="Пароль:", font=label_font, bg="white", fg="black").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_password = tk.Entry(self, font=label_font, bd=2, relief="solid", show="*", width=30)
        self.entry_password.grid(row=1, column=1, padx=20, pady=10)

        # Кнопка "Войти"
        login_button = tk.Button(self, text="Войти", font=button_font, command=self.login, bg="#03DAC5", fg="white", relief="flat")
        login_button.grid(row=2, columnspan=2, pady=20)

        # Кнопка "Назад к регистрации"
        back_button = tk.Button(self, text="Назад к регистрации", font=button_font, command=self.go_to_registration, bg="#B00020", fg="white", relief="flat")
        back_button.grid(row=3, columnspan=2, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)


    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Вызов метода для авторизации
        self.user_view_model.login(email, password, self.handle_login_result)
        self.save_uid(email)  # Сохраняем UID
    def handle_login_result(self, result):
        """Обрабатывает результат авторизации."""
        if isinstance(result, dict) and result.get('status') is True and 'uid' in result:
            # Успешный вход
            uid = result['uid']

            messagebox.showinfo("Успех", f"Вход выполнен успешно! UID: {uid}")
            self.destroy()
            self.controller.show_screen("game")  # Переход на главный экран
        else:
            # Ошибка при авторизации
            messagebox.showerror("Ошибка", "Неправильный Email или пароль!")


    def save_uid(self, uid):
        """Сохраняет UID в файл в указанной директории."""
        try:
            # Проверяем, существует ли директория, если нет — создаем
            os.makedirs(self.data_directory, exist_ok=True)

            # Записываем UID в файл (перезаписываем, если уже существует)
            with open(self.uid_file, 'w') as file:
                file.write(uid)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить UID: {e}")

    def go_to_registration(self):
        """Метод для перехода на экран регистрации."""
        from UserScreen.RegistrationScreen import RegistrationScreen  # Импорт экрана регистрации
        self.destroy()  # Удаляем текущий экран
        RegistrationScreen(self.root, self.controller).pack(expand=True, fill="both")
