import datetime
import os


class DateProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            for line in file.readlines():
                yield line

    def process_line(self, line):
        parts = line.split(' - ')  # Разбивает строку на части по разделителю ' - '
        date_str = parts[0].split('. ')[1]  # Извлекает дату из первой части строки
        date = datetime.datetime.fromisoformat(date_str)  # Преобразует строку в объект datetime
        task_number = int(parts[0].split('. ')[0])  # Извлекает номер задачи
        if task_number == 1:
            self.add_week(date)
        elif task_number == 2:
            self.print_day_of_week(date)
        elif task_number == 3:
            self.print_days_ago(date)

    @staticmethod
    def add_week(date):
        new_date = date + datetime.timedelta(weeks=1)
        print(new_date)

    @staticmethod
    def print_day_of_week(date):
        day_of_week = date.strftime('%A')
        print(day_of_week)

    @staticmethod
    def print_days_ago(date):
        now = datetime.datetime.now()
        days_passed = (now - date).days
        print(days_passed)

    def process_dates(self):
        for line in self.read_file():
            self.process_line(line)


# Построение пути к файлу
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
date_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

# Создаем экземпляр класса и запускаем обработку дат
processor = DateProcessor(date_file_path)
processor.process_dates()
