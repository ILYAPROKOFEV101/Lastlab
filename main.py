# This is a sample Python script.
import os
from tkinter import messagebox

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Основной код
from UserScreen.LoginScreen import LoginScreen
from UserScreen.RegistrationScreen import RegistrationScreen
from UserScreen.go import Go
from ViewModel.ScreenControler import ScreenController

import tkinter as tk

from UserScreen.rock_from_fortnite import GameScreen




def check_uid():
    """Проверяет наличие UID в файле."""
    data_directory = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data"
    uid_file = os.path.join(data_directory, "uid.txt")

    # Проверяем, существует ли файл с UID
    if os.path.exists(uid_file):
        try:
            with open(uid_file, 'r') as file:
                uid = file.read().strip()
                if uid:  # Если UID не пустой
                    return True
        except Exception:
            pass
    return False




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Screen Controller")

    # Создаем контроллер экранов
    controller = ScreenController(root)

    # Создаем экраны
    register_screen = RegistrationScreen(root, controller)
    login_screen = LoginScreen(root, controller)
    game_screen = GameScreen(root, controller)
    Goto = Go(root, controller)

    # Добавляем экраны в контроллер
    controller.add_screen("login", login_screen)
    controller.add_screen("register", register_screen)
    controller.add_screen("game", game_screen)
    controller.add_screen("go", Goto)


    controller.show_screen("go")  # Если UID нет, показываем экран регистрации

root.mainloop()
