import tkinter as tk
from tkinter import messagebox
import random
from tkinter import Tk, Label, Frame, Button
import tkinter as tk
from tkinter import messagebox
import random
from tkinter import Tk, Label, Frame, Button
from PIL import Image, ImageTk
from PIL import Image, ImageTk

# Список для хранения статистики игры
history = []
player_choices = {"rock": 0, "scissors": 0, "paiper": 0}
game_number = 0  # Номер игры


def save_game_result(result_text):
    with open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\history.txt", 'a', encoding='utf-8') as file:
        file.write(result_text + "\n")


# Функция для обработки выбора игрока
def player_choice(choice):
    global game_number  # Чтобы обновить номер игры
    player_choices[choice] += 1
    game_number += 1  # Увеличиваем номер игры
    computer_choice = intelligent_choice()

    # Загружаем изображения для кнопок
    if computer_choice == "rock":
        computer_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\rock.png").resize((80, 80)))
    elif computer_choice == "scissors":
        computer_image = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\scissors.png").resize((80, 80)))
    else:
        computer_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\paiper.png").resize((80, 80)))

    computer_label.config(text="Компьютер выбрал:")
    computer_choice_label.config(image=computer_image)
    computer_choice_label.image = computer_image

    if choice == computer_choice:
        result = "Ничья!"
    elif (choice == "rock" and computer_choice == "scissors") or \
            (choice == "scissors" and computer_choice == "paiper") or \
            (choice == "paiper" and computer_choice == "rock"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"


    result_label.config(text=result)
    history.append(f"Игра {game_number}: Игрок: {choice.capitalize()}, Компьютер: {computer_choice.capitalize()}, Результат: {result}")
    # Формируем строку результата и сохраняем в файл
    result_text = f"Игра {game_number}: Игрок: {choice.capitalize()}, Компьютер: {computer_choice.capitalize()}, Результат: {result}"
    save_game_result(result_text)
    update_history()

def on_rock_button_click():
    player_choice("rock")

def on_scissors_button_click():
    player_choice("scissors")

def on_paper_button_click():
    player_choice("paiper")

def intelligent_choice():
    most_chosen = max(player_choices, key=player_choices.get)
    if most_chosen == "rock":
        return "paiper"
    elif most_chosen == "scissors":
        return "rock"
    elif most_chosen == "paiper":
        return "scissors"
    return random.choice(["rock", "scissors", "paiper"])



# Функция для обновления статистики в интерфейсе
def update_history():
    # Очищаем текущую статистику
    history_text.delete(1.0, tk.END)

    # Добавляем название игры в начало
    history_text.insert(tk.END, "Игра: Камень, Ножницы, Бумага\n\n")

    # Выводим историю в текстовое поле
    for step in history:
        history_text.insert(tk.END, step + "\n")


# Создание основного окна
root = tk.Tk()
root.title("Камень, Ножницы, Бумага")

# Создаём фоновое изображение и масштабируем его
background_image = Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\RPS.png")
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Масштабирование под размер экрана
background_image = ImageTk.PhotoImage(background_image)

background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Расширяем фон на весь экран

# Центрируем главный фрейм с фоном и рамкой
main_frame = tk.Frame(root, bg="lightblue", bd=5, relief="solid")  # Добавляем цвет фона и рамку
main_frame.pack(expand=True, padx=20, pady=20)

# Фрейм для кнопок выбора с фоном и рамкой
button_frame = tk.Frame(main_frame, bg="lightgray", bd=2, relief="groove")

# Загружаем изображения для кнопок
rock_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\paiper.png").resize((80, 80)))
scissors_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\scissors.png").resize((80, 80)))
paper_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\paiper.png").resize((80, 80)))

# Кнопки для выбора игрока с отключённой подсветкой и рамкой
rock_button = tk.Button(button_frame, image=rock_image, command=on_rock_button_click, relief="flat", bd=0)
rock_button.grid(row=0, column=0, padx=10, pady=5)

scissors_button = tk.Button(button_frame, image=scissors_image, command=on_scissors_button_click, relief="flat", bd=0)
scissors_button.grid(row=0, column=1, padx=10, pady=5)

paper_button = tk.Button(button_frame, image=paper_image, command=on_paper_button_click, relief="flat", bd=0)
paper_button.grid(row=0, column=2, padx=10, pady=5)

# Метка для отображения выбора компьютера
computer_label = tk.Label(main_frame, text="Компьютер выбрал:", font=("Helvetica", 14))
computer_label.pack(pady=10)

# Метка для отображения изображения выбора компьютера
computer_choice_label = tk.Label(main_frame)
computer_choice_label.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(main_frame, text="Результат: ", font=("Helvetica", 14))
result_label.pack(pady=10)


history_text = tk.Text(main_frame, width=70, height=10)
history_text.pack(pady=10)

# Инструкция для выбора хода
instruction_label = tk.Label(main_frame, text="Выберите свой ход", font=("Helvetica", 14))
instruction_label.pack(pady=50)

# Вызов кнопок игры
button_frame.pack(pady=10)

# Запуск главного цикла
root.mainloop()