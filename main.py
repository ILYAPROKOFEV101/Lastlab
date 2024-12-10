# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Основной код
from UserScreen.LoginScreen import LoginScreen
from UserScreen.RegistrationScreen import RegistrationScreen
from ViewModel.ScreenControler import ScreenController

import tkinter as tk

from UserScreen.rock_from_fortnite import GameScreen

def check_uid():
    """Проверяет, существует ли UID в файле."""
    uid_file = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data\uid.txt"
    if os.path.exists(uid_file):
        with open(uid_file, "r") as file:
            uid = file.read().strip()
            if uid:  # Проверяем, что UID не пустой
                return True
    return False
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Controller")

    controller = ScreenController(root)

    # Создаем экраны
    register_screen = RegistrationScreen(root, controller)
    login_screen = LoginScreen(root, controller)
    game_screen = GameScreen(root, controller)

    # Добавляем экраны в контроллер
    controller.add_screen("login", login_screen)
    controller.add_screen("register", register_screen)
    controller.add_screen("game", game_screen)

    # Проверяем UID и показываем нужный экран
    if check_uid():
        controller.show_screen("game")  # Если UID найден, сразу переходим в игру
    else:
        controller.show_screen("register")  # Если UID нет, показываем экран регистрации

    root.mainloop()

