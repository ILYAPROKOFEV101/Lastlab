# This is a sample Python script.
import tkinter as tk

from UserScreen.LoginScreen import LoginScreen
from UserScreen.RegistrationScreen import RegistrationScreen
from ViewModel.ScreenControler import ScreenController

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Основной код
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Controller")

    controller = ScreenController(root)

    # Создаем экраны
    register_screen = RegistrationScreen(root, controller)
    login_screen = LoginScreen(root, controller)

    # Добавляем экраны в контроллер
    controller.add_screen("login", login_screen)
    controller.add_screen("register", register_screen)

    # Показываем экран регистрации по умолчанию
    controller.show_screen("register")

    root.mainloop()
