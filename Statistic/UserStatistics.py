import json
import os

import json

import os


import os
import json

class StatisticsManager:
    def __init__(self):
        self.stats_file_path = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\res\stats.txt"
        self.uid_file_path = r"C:\Users\Ilya\PycharmProjects\PPSGAMEV2\data\uid.txt"

        # Загружаем UID из файла
        self.uid = self.load_uid()

        # Если файл статистики существует и не пуст, загружаем статистику, иначе создаем пустой объект
        if os.path.exists(self.stats_file_path) and os.path.getsize(self.stats_file_path) > 0:
            with open(self.stats_file_path, 'r') as file:
                self.stats = json.load(file)
        else:
            self.stats = {}  # Если файл пуст или не существует, создаем пустой словарь

        # Убедимся, что файл статистики существует, если нет - создадим его
        if not os.path.exists(self.stats_file_path):
            with open(self.stats_file_path, 'w') as file:
                json.dump(self.stats, file, indent=4)

    def load_uid(self):
        """Загружает UID из файла."""
        if os.path.exists(self.uid_file_path):
            with open(self.uid_file_path, 'r') as file:
                uid = file.read().strip()  # Читаем UID из файла и убираем лишние пробелы
                print(f"Загружен UID: {uid}")  # Отладочная информация
                return uid
        return None  # Если UID не найден, возвращаем None

    def save_statistics(self, wins, games_played, player_choices, computer_choices):
        """Сохраняет или обновляет статистику для данного UID."""
        if not self.uid:
            raise ValueError("UID is not found in the uid file.")  # Выбрасываем ошибку, если UID не найден

        # Если для этого UID уже есть статистика, обновляем ее
        if self.uid in self.stats:
            self.stats[self.uid]['wins'] += wins
            self.stats[self.uid]['games_played'] += games_played
            self.stats[self.uid]['player_choices'] = player_choices
            self.stats[self.uid]['computer_choices'] = computer_choices
        else:
            # Если статистики для этого UID нет, создаем новую запись
            self.stats[self.uid] = {
                'wins': wins,
                'games_played': games_played,
                'player_choices': player_choices,
                'computer_choices': computer_choices
            }

        # Сохраняем статистику обратно в файл
        with open(self.stats_file_path, 'w') as file:
            json.dump(self.stats, file, indent=4)

    def get_statistics(self):
        """Возвращает статистику для текущего UID."""
        if not self.uid:
            raise ValueError("UID is not found in the uid file.")  # Выбрасываем ошибку, если UID не найден

        return self.stats.get(self.uid, None)

