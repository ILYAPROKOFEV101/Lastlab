import tkinter as tk
from tkinter import messagebox

class RegistrationScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller
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

        # Вывод данных для демонстрации
        user_data = {
            "name": name,
            "email": email,
            "password": password,
            "gender": gender,
            "age": age
        }
        messagebox.showinfo("Успех", f"Регистрация прошла успешно!\nДанные: {user_data}")

    def go_to_login(self):
        """Метод для перехода на экран входа."""
        from UserScreen.LoginScreen import LoginScreen  # Отложенный импорт
        self.destroy()  # Удаляем текущий экран
        login_screen = LoginScreen(self.root, self.controller)  # Передаем controller
        login_screen.pack(expand=True, fill="both")
