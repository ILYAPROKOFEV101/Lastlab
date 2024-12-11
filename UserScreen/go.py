from tkinter import ttk

from IPython.terminal.pt_inputhooks import tk

from ViewModel.UserViewModel import UserViewModel

import tkinter as tk
from tkinter import ttk


class Go(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller

        # Настройка строки и столбца для растяжения
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Вызываем метод для создания виджетов
        self.create_widgets()

    def create_widgets(self):
        """Создание виджетов на экране"""

        # Кнопка "Начать"
        submit_button = ttk.Button(self, text="Начать", command=self.handle_login_result)
        submit_button.grid(row=0, column=0, sticky="nsew")  # Растягиваем кнопку на весь экран

    def handle_login_result(self):
        """Обрабатывает результат нажатия кнопки"""

        # Переход на экран регистрации
        self.controller.show_screen("register")  # Переход на экран регистрации

        # Удаление текущего экрана, если необходимо
        self.destroy()
