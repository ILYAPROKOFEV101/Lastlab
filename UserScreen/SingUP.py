import tkinter as tk
from tkinter import messagebox


def submit():
    # Получаем данные из полей ввода
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    age = entry_age.get()

    # Проверка на корректность ввода
    if not name or not email or not password or not gender or not age:
        messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
        return

    # Вывод данных для демонстрации
    user_data = {
        "name": name,
        "email": email,
        "password": password,
        "gender": gender,
        "age": age
    }
    messagebox.showinfo("Успех", f"Регистрация прошла успешно!\nДанные: {user_data}")


# Создаем главное окно
root = tk.Tk()
root.title("Регистрация")
root.geometry("300x300")

# Метки и поля ввода
tk.Label(root, text="Имя:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Пароль:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Пол:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="male")
gender_menu = tk.OptionMenu(root, gender_var, "male", "female", "other")
gender_menu.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Возраст:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(root)
entry_age.grid(row=4, column=1, padx=10, pady=5)

# Кнопка для отправки данных
submit_button = tk.Button(root, text="Регистрация", command=submit)
submit_button.grid(row=5, columnspan=2, pady=20)

# Запуск главного цикла приложения
root.mainloop()
