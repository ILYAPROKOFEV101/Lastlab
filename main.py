# This is a sample Python script.
import tkinter as tk

from UserScreen.LoginScreen import LoginScreen
from UserScreen.RegistrationScreen import RegistrationScreen
from ViewModel.ScreenControler import ScreenController

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Основной код
from UserScreen.LoginScreen import LoginScreen
from UserScreen.RegistrationScreen import RegistrationScreen
from ViewModel.ScreenControler import ScreenController

import tkinter as tk

from rock_from_fortnite import GameScreen

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

    # Показываем экран регистрации по умолчанию
    controller.show_screen("game")

    root.mainloop()

