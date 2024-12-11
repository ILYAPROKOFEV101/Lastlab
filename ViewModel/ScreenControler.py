import tkinter as tk

class ScreenController:
    def __init__(self, root):
        self.root = root
        self.screens = {}  # Словарь для хранения экранов
        self.current_screen = None

    def add_screen(self, name, screen):
        """Добавляем экран в словарь."""
        self.screens[name] = screen

    def show_screen(self, screen_name):
        """Метод для отображения экрана по имени."""
        if self.current_screen is not None:
            self.current_screen.pack_forget()  # Скрываем текущий экран
        self.current_screen = self.screens[screen_name]
        self.current_screen.pack(expand=True, fill="both")  # Показываем новый экран

        # Устанавливаем размер окна в зависимости от текущего экрана
        self.set_screen_size(screen_name)

    def set_screen_size(self, screen_name):
        """Устанавливаем размеры окна и заголовок в зависимости от экрана"""
        if screen_name == "login":
            self.root.geometry("500x350")  # Размер для экрана входа
            self.root.configure(bg="lightblue")  # Устанавливаем фон окна
            self.root.title("Вход в игру")  # Устанавливаем заголовок окна
        elif screen_name == "register":
            self.root.geometry("500x370")  # Размер для экрана регистрации
            self.root.configure(bg="lightblue")  # Устанавливаем фон окна
            self.root.title("Регистрация")  # Устанавливаем заголовок окна

        elif screen_name == "game":
            self.root.geometry("1100x690")  # Размер для игрового экрана
            self.root.configure(bg="lightblue")  # Устанавливаем фон окна
            self.root.title("Игровой экран")  # Устанавливаем заголовок окна
        elif screen_name == "go":
            self.root.geometry("1100x690")  # Размер для игрового экрана
            self.root.configure(bg="lightblue")  # Устанавливаем фон окна
            self.root.title("Поехали")  # Устанавливаем заголовок окна
