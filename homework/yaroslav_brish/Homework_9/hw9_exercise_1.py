# Задание №1

# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"


from datetime import datetime


date_string = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_object = datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")

# Получение полного названия месяца и даты в требуемом формате
month_full_name = date_object.strftime("%B")
formatted_date = date_object.strftime("%d.%m.%Y, %H:%M")

print(f"Месяц: {month_full_name}")
print(f"Дата: {formatted_date}")
