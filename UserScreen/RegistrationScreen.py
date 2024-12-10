import tkinter as tk
from tkinter import messagebox, ttk

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
        # Стилизация
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#f4f4f4")
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TEntry", font=("Arial", 12))
        # Настройка стиля для Entry
        style.configure("TEntry", bd=2, relief="solid")

        # Настройка стиля для Combobox
        style.configure("TCombobox", bd=2, relief="solid")

        # Заголовок
        title_label = tk.Label(self, text="Регистрация", font=("Arial", 20, "bold"), bg="#f4f4f4")
        title_label.pack(pady=10)

        # Поля ввода
        form_frame = ttk.Frame(self, padding=(20, 10))  # Используем ttk.Frame
        form_frame.pack(fill="x", pady=10)

        # Устанавливаем вес для колонок, чтобы поля занимали больше места
        form_frame.grid_columnconfigure(1, weight=1, uniform="equal")



        # Настроим шрифт для меток и полей ввода
        label_font = ('Arial', 12)

        # Поля ввода
        tk.Label(form_frame, text="Имя:", font=label_font).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(form_frame, font=label_font, bd=2, relief="solid", width=30)
        self.entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(form_frame, text="Email:", font=label_font).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_email = tk.Entry(form_frame, font=label_font, bd=2, relief="solid", width=30)
        self.entry_email.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(form_frame, text="Пароль:", font=label_font).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_password = tk.Entry(form_frame, font=label_font, show="*", bd=2, relief="solid", width=30)
        self.entry_password.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(form_frame, text="Пол:", font=label_font).grid(row=3, column=0, sticky="w", pady=5)
        self.gender_var = tk.StringVar(value="Мужской")
        gender_menu = tk.OptionMenu(form_frame, self.gender_var, "Мужской", "Женский")
        gender_menu.grid(row=3, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(form_frame, text="Возраст:", font=label_font).grid(row=4, column=0, sticky="w", pady=5)
        self.entry_age = tk.Entry(form_frame, font=label_font, bd=2, relief="solid", width=30)
        self.entry_age.grid(row=4, column=1, pady=5, padx=10, sticky="ew")

        # Кнопки
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        submit_button = ttk.Button(button_frame, text="Регистрация", command=self.submit)
        submit_button.grid(row=0, column=0, padx=10)

        login_button = ttk.Button(button_frame, text="Войти", command=self.go_to_login)
        login_button.grid(row=0, column=1, padx=10)

    def submit(self):
        # Получаем данные из полей ввода
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()
        gender = self.gender_var.get().strip()
        age = self.entry_age.get().strip()

        # Проверка: все поля должны быть заполнены
        if not all([name, email, password, gender, age]):
            messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
            return

        # Проверка имени (минимум 2 символа, только буквы)
        import re
        if not re.fullmatch(r"[A-Za-zА-Яа-я\s]{2,}", name):
            messagebox.showwarning("Ошибка", "Имя должно содержать только буквы и быть не короче 2 символов!")
            return

        # Проверка email (основной формат email)
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Ошибка", "Введите корректный адрес электронной почты!")
            return

        # Проверка пароля (минимум 6 символов, хотя бы одна цифра и одна буква)
        if len(password) < 6:
            messagebox.showwarning("Ошибка", "Пароль должен быть не менее 6 символов и содержать буквы и цифры!")
            return

        # Проверка возраста (число от 1 до 120)
        if not age.isdigit() or not (1 <= int(age) <= 120):
            messagebox.showwarning("Ошибка", "Возраст должен быть числом от 1 до 120!")
            return

        # Если все проверки пройдены, вызываем метод для регистрации
        self.user_view_model.create_user(
            name, email, password, gender, age, self.handle_registration_result
        )
        self.save_uid(email)  # Сохраняем UID

    def handle_registration_result(self, result):
        """Обрабатывает результат регистрации."""
        if isinstance(result, dict) and result.get("status") is True and "uid" in result:
            uid = result["uid"]

            messagebox.showinfo("Успех", f"Вход выполнен успешно! UID: {uid}")

            self.controller.show_screen("game")  # Переход на экран входа
            self.destroy()  # Удаляем текущий экран
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
