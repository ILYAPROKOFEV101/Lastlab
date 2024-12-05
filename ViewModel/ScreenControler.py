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
