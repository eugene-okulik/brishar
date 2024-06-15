import mysql.connector as mysql
import os
import dotenv
import csv


# Загрузка переменных окружения из файла .env
dotenv.load_dotenv()


# Подключение к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

# Путь к CSV файлу
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = (os.path.join(
    homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
)  # Пришлось разнести на несколько строк, т.к. ругался линтер из-за длины строки...

# Чтение данных из CSV файла
with open(csv_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    csv_data = list(file_data)

# Проверка наличия данных в базе данных
missing_data = []

for row in csv_data:
    query = """
    SELECT
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        sub.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark_value
    FROM
        students s
    LEFT JOIN
        `groups` g ON s.group_id = g.id
    LEFT JOIN
        books b ON s.id = b.taken_by_student_id
    LEFT JOIN
        marks m ON s.id = m.student_id
    LEFT JOIN
        lessons l ON m.lesson_id = l.id
    LEFT JOIN
        subjets sub ON l.subject_id = sub.id
    WHERE
        s.name = %s AND
        s.second_name = %s AND
        g.title = %s AND
        b.title = %s AND
        sub.title = %s AND
        l.title = %s AND
        m.value = %s
    """

    cursor.execute(query, (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    ))

    result = cursor.fetchone()
    if not result:
        missing_data.append(row)

# Закрытие курсора и соединения с базой данных
cursor.close()
db.close()

# Вывод данных, которых не хватает в базе данных
if missing_data:
    print("Следующих данных нет в базе данных:")
    for data in missing_data:
        print(data)
else:
    print("Все данные из CSV файла присутствуют в базе данных.")
