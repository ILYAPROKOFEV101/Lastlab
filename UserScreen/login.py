import tkinter as tk
from tkinter import messagebox

def login():
    # Получаем данные из полей ввода
    email = entry_email.get()
    password = entry_password.get()

    # Проверка на корректность ввода
    if not email or not password:
        messagebox.showwarning("Ошибка", "Оба поля должны быть заполнены!")
        return

    # Пример логики проверки (можно заменить на вашу)
    if email == "ilya@example.com" and password == "ilyatop":
        messagebox.showinfo("Успех", "Авторизация прошла успешно!")
    else:
        messagebox.showerror("Ошибка", "Неправильный Email или пароль!")

# Создаем главное окно
root = tk.Tk()
root.title("Авторизация")
root.geometry("300x200")

# Метки и поля ввода
tk.Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для входа
login_button = tk.Button(root, text="Войти", command=login)
login_button.grid(row=2, columnspan=2, pady=20)

# Запуск главного цикла приложения
root.mainloop()
