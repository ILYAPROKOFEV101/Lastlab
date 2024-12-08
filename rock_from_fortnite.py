import os
import random
import tkinter as tk
from tkinter import Label, Frame, Button, Text
from PIL import Image, ImageTk

class GameScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.controller = controller

        self.history = []
        self.player_choices = {"rock": 0, "scissors": 0, "paper": 0}
        self.game_number = 0  # Номер игры
        self.data_directory = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res"
        self.history_file = os.path.join(self.data_directory, "history.txt")
        self.create_widgets()

    def create_widgets(self):


        # Главный фрейм
        main_frame = Frame(self, bg="lightblue", bd=5, relief="solid")
        main_frame.pack(expand=True, padx=20, pady=20)

        # Кнопки выбора
        button_frame = Frame(main_frame, bg="lightgray", bd=2, relief="groove")

        rock_image = ImageTk.PhotoImage(Image.open(os.path.join(self.data_directory, "rock.png")).resize((80, 80)))
        scissors_image = ImageTk.PhotoImage(Image.open(os.path.join(self.data_directory, "scissors.png")).resize((80, 80)))
        paper_image = ImageTk.PhotoImage(Image.open(os.path.join(self.data_directory, "paiper.png")).resize((80, 80)))

        rock_button = Button(button_frame, image=rock_image, command=lambda: self.player_choice("rock"), relief="flat", bd=0)
        rock_button.image = rock_image
        rock_button.grid(row=0, column=0, padx=10, pady=5)

        scissors_button = Button(button_frame, image=scissors_image, command=lambda: self.player_choice("scissors"), relief="flat", bd=0)
        scissors_button.image = scissors_image
        scissors_button.grid(row=0, column=1, padx=10, pady=5)

        paper_button = Button(button_frame, image=paper_image, command=lambda: self.player_choice("paper"), relief="flat", bd=0)
        paper_button.image = paper_image
        paper_button.grid(row=0, column=2, padx=10, pady=5)

        button_frame.pack(pady=10)

        # Метки
        self.computer_label = Label(main_frame, text="Компьютер выбрал:", font=("Helvetica", 14))
        self.computer_label.pack(pady=10)

        self.computer_choice_label = Label(main_frame)
        self.computer_choice_label.pack(pady=10)

        self.result_label = Label(main_frame, text="Результат: ", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        # История
        self.history_text = Text(main_frame, width=70, height=10)
        self.history_text.pack(pady=10)

    def player_choice(self, choice):
        """Обработка выбора игрока."""
        self.player_choices[choice] += 1
        self.game_number += 1
        computer_choice = self.intelligent_choice()

        # Загружаем изображение выбора компьютера
        choice_image_path = os.path.join(self.data_directory, f"{computer_choice}.png")
        computer_image = ImageTk.PhotoImage(Image.open(choice_image_path).resize((80, 80)))
        self.computer_choice_label.config(image=computer_image)
        self.computer_choice_label.image = computer_image

        # Логика результата
        if choice == computer_choice:
            result = "Ничья!"
        elif (choice == "rock" and computer_choice == "scissors") or \
             (choice == "scissors" and computer_choice == "paper") or \
             (choice == "paper" and computer_choice == "rock"):
            result = "Вы победили!"
        else:
            result = "Вы проиграли!"

        self.result_label.config(text=result)
        self.history.append(f"Игра {self.game_number}: Игрок: {choice}, Компьютер: {computer_choice}, Результат: {result}")
        self.save_game_result(f"Игра {self.game_number}: Игрок: {choice}, Компьютер: {computer_choice}, Результат: {result}")
        self.update_history()

    def intelligent_choice(self):
        """Выбор компьютера с использованием статистики."""
        most_chosen = max(self.player_choices, key=self.player_choices.get)
        if most_chosen == "rock":
            return "paper"
        elif most_chosen == "scissors":
            return "rock"
        elif most_chosen == "paper":
            return "scissors"
        return random.choice(["rock", "scissors", "paper"])

    def save_game_result(self, result_text):
        """Сохранение результатов в файл."""
        try:
            with open(self.history_file, 'a', encoding='utf-8') as file:
                file.write(result_text + "\n")
        except Exception as e:
            print(f"Ошибка сохранения истории: {e}")

    def update_history(self):
        """Обновление истории на экране."""
        self.history_text.delete(1.0, tk.END)
        for step in self.history:
            self.history_text.insert(tk.END, step + "\n")
