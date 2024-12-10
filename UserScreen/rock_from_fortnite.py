import json
import os
import random
import tkinter as tk
from tkinter import Label, Frame, Button, Text, messagebox,Scrollbar
from PIL import Image, ImageTk

import os

from Statistic.UserStatistics import StatisticsManager


def delete_uid():
    """Удаление UID из файла."""
    uid_file = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data\uid.txt"
    try:
        with open(uid_file, 'r') as file:
            lines = file.readlines()

        # Удаляем последнюю строку (если это UID)
        if lines:
            lines.pop()

        with open(uid_file, 'w') as file:
            file.writelines(lines)
        print("UID удален")
    except Exception as e:
        print(f"Ошибка при удалении UID: {e}")


class GameScreen(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root

        self.controller = controller

        self.history = []
        self.player_choices = {"rock": 0, "scissors": 0, "paper": 0}
        self.computer_choices = {"rock": 0, "scissors": 0, "paper": 0}
        self.games_played = 0  # Инициализируем количество игр
        self.game_number = 0  # Номер игры
        self.wins = 0  # Количество побед
        self.data_directory = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res"
        self.history_file = os.path.join(self.data_directory, "history.txt")
        # Инициализация атрибутов статистики
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0
        # Инициализация stats_manager здесь
        self.stats_manager = StatisticsManager()
        self.create_widgets()

    def create_widgets(self):
        # Главный фрейм
        main_frame = Frame(self, bg="lightblue", bd=0, relief="solid")
        main_frame.pack(expand=True, padx=20, pady=20)

        # Разделим экран на 2 части
        left_frame = Frame(main_frame, bg="lightblue")
        left_frame.grid(row=0, column=0, padx=20, pady=20)

        right_frame = Frame(main_frame, bg="lightblue")
        right_frame.grid(row=0, column=1, padx=20, pady=20)

        # Кнопка "Выйти"
        exit_button = Button(left_frame, text="Выйти", command=self.exit_game)
        exit_button.pack(pady=1)

        self.save_button = Button(left_frame, text="Сохронить Игру", command=self.save_game_statistics)
        self.save_button.pack(pady=1)

        self.new_game = Button(left_frame, text="Новая Игра", command=self.start_new_game)
        self.new_game.pack()

        # Кнопки выбора
        button_frame = Frame(left_frame, bg="lightblue", relief="groove")
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

        # Метки с синим фоном и белым текстом
        self.computer_label = Label(left_frame, text="Компьютер выбрал:", font=("Helvetica", 14), bg="lightblue", fg="white")
        self.computer_label.pack(pady=10)

        self.computer_choice_label = Label(left_frame, bg="lightblue", fg="white")
        self.computer_choice_label.pack(pady=10)

        self.result_label = Label(left_frame, text="Результат: ", font=("Helvetica", 14), bg="lightblue", fg="white")
        self.result_label.pack(pady=10)

        # История
        self.history_text = Text(main_frame, width=70, height=0)


        # Статистика (правый фрейм)
        self.stats_label = Label(left_frame, text="Статистика: ", font=("Helvetica", 14), bg="lightblue", fg="white")
        self.stats_label.pack(pady=10)

        self.stats_text = Label(left_frame, text="", font=("Helvetica", 12), bg="lightblue", fg="white")
        self.stats_text.pack(pady=10)

        # Создаем метки для вывода статистики
        self.stats_frame = tk.Frame(right_frame)
        self.stats_frame.pack(padx=10, pady=10)

        # Добавляем полосу прокрутки
        # Создаем виджет Text для прокрутки статистики
        self.stats_text_widget = Text(right_frame, height=20, width=60,font=("Helvetica", 14), bg="lightblue", fg="white")
        self.stats_text_widget.pack(padx=10, pady=10)

        # Добавляем полосу прокрутки
        scrollbar = Scrollbar(right_frame, command=self.stats_text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        self.stats_text_widget.config(yscrollcommand=scrollbar.set)

        # Чтение и отображение статистики
        self.read_and_display_statistics("C:/Users/Ilya/PycharmProjects/PPSGAMEV2/res/stats.txt")


    def player_choice(self, choice):
        """Обработка выбора игрока."""
        self.player_choices[choice] += 1
        self.game_number += 1
        computer_choice = self.intelligent_choice()
        self.computer_choices[computer_choice] += 1

        # Загружаем изображение выбора компьютера
        if computer_choice == "paper":
            choice_image_path = os.path.join(self.data_directory, "paiper.png")  # Используем 'paiper.png' для paper
        else:
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
            self.wins += 1
        else:
            result = "Вы проиграли!"

        self.result_label.config(text=result)
        self.history.append(
            f"Игра {self.game_number}: Игрок: {choice}, Компьютер: {computer_choice}, Результат: {result}")
        self.save_game_result(
            f"Игра {self.game_number}: Игрок: {choice}, Компьютер: {computer_choice}, Результат: {result}")
        self.update_history()
        self.update_stats()
        self.update_games_played()

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

    # Функция, которая увеличивает количество сыгранных игр, например, после каждой игры
    def update_games_played(self):
        self.games_played += 1

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

    def update_stats(self):
        """Обновление статистики на экране."""
        total_games = self.game_number
        if total_games == 0:
            player_rock_percent = player_scissors_percent = player_paper_percent = 0
            win_percent = 0
        else:
            player_rock_percent = round((self.player_choices["rock"] / total_games) * 100)
            player_scissors_percent = round((self.player_choices["scissors"] / total_games) * 100)
            player_paper_percent = round((self.player_choices["paper"] / total_games) * 100)
            win_percent = round((self.wins / total_games) * 100)

        stats_text = (
            f"Игры сыграно: {self.games_played}\n\n"
            f"Выбор игрока (процент):\n"
            f"Камень: {player_rock_percent}%\n"
            f"Ножницы: {player_scissors_percent}%\n"
            f"Бумага: {player_paper_percent}%\n\n"
            f"Процент побед: {win_percent}%"
        )
        self.stats_text.config(text=stats_text)

    def exit_game(self):
        """Метод для выхода из игры с подтверждением."""
        # Показываем диалог с вопросом
        response = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите выйти?")

        if response:  # Если пользователь нажал 'Yes'
            self.destroy()  # Удаляем текущий экран
            delete_uid()  # Вызов функции для удаления UID
            self.controller.show_screen("login")  # Переход на экран входа
        else:
            return  # Если пользователь нажал 'No', просто ничего не делаем

    def check_winner(self, player_choice, computer_choice):
        """Проверка победителя игры."""
        win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        if player_choice == computer_choice:
            return False
        return win_conditions[player_choice] == computer_choice

    def start_new_game(self):
        """Сбросить статистику и начать новую игру"""
        self.player_choices = {"rock": 0, "scissors": 0, "paper": 0}
        self.computer_choices = {"rock": 0, "scissors": 0, "paper": 0}
        self.games_played = 0  # Сбросить количество сыгранных игр
        self.game_number = 0  # Сбросить номер игры
        self.wins = 0  # Сбросить количество побед
        self.player_wins = 0  # Сбросить победы игрока
        self.computer_wins = 0  # Сбросить победы компьютера
        self.draws = 0  # Сбросить количество ничьих



    def save_game_statistics(self):
        """
        Сохраняет всю информацию о текущей игре в файл статистики и истории.
        """
        try:
            # Убедимся, что UID загружен в stats_manager
            if not self.stats_manager.uid:
                raise ValueError("UID not found. Make sure UID is saved in the file.")

            # Сохраняем статистику игрока, больше не передаем UID
            self.stats_manager.save_statistics(self.wins, self.games_played, self.player_choices, self.computer_choices)

            # Дополнительная информация (выборы игрока и компьютера)
            with open(self.history_file, 'a') as file:
                file.write(f"\n--- Game {self.game_number} ---\n")
                file.write(f"Player Choices: {self.player_choices}\n")
                file.write(f"Computer Choices: {self.computer_choices}\n")
                file.write(f"Games Played: {self.games_played}\n")
                file.write(f"Games Won: {self.wins}\n")

            messagebox.showinfo("Saved", "Game statistics have been saved.")
        except AttributeError as e:
            messagebox.showerror("Error", f"Error saving game statistics: {str(e)}")
        except ValueError as e:
            messagebox.showerror("Error", f"UID Error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")


        self.read_and_display_statistics("C:/Users/Ilya/PycharmProjects/PPSGAMEV2/res/stats.txt")

    def read_and_display_statistics(self, file_path):
        try:
            # Открытие файла и загрузка данных
            with open(file_path, "r", encoding="utf-8") as file:
                stats_data = json.load(file)

            # Очищаем текстовое поле перед добавлением новых данных
            self.stats_text_widget.delete(1.0, tk.END)

            # Добавление статистики в Text
            for player, stats in stats_data.items():
                self.stats_text_widget.insert(tk.END, f"Статистика для {player}:\n")
                self.stats_text_widget.insert(tk.END, f"  Победы: {stats['wins']}\n")
                self.stats_text_widget.insert(tk.END, f"  Сыграно игр: {stats['games_played']}\n")
                self.stats_text_widget.insert(tk.END, f"  Выборы игрока:\n")
                for choice, count in stats['player_choices'].items():
                    self.stats_text_widget.insert(tk.END, f"    {choice.capitalize()}: {count}\n")
                self.stats_text_widget.insert(tk.END, f"  Выборы компьютера:\n")
                for choice, count in stats['computer_choices'].items():
                    self.stats_text_widget.insert(tk.END, f"    {choice.capitalize()}: {count}\n")
                self.stats_text_widget.insert(tk.END, "\n")

        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Ошибка: {e}")
