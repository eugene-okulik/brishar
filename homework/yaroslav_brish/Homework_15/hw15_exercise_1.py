import mysql.connector as mysql

# подключение к БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создаем студента
query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('John1', 'Wick1')
cursor.execute(query, values)
student_id = cursor.lastrowid  # сохраняем id студента в переменную

# Создаем группу
query = \
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('The Killers1', 'may 2024', 'aug 2024')
cursor.execute(query, values)
group_id = cursor.lastrowid  # сохраняем id группы в переменную

# Обновляем запись студента, чтобы присвоить ему group_id
query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)

# Создаем несколько книг (books) и указываем, что наш созданный студент взял их
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('How To Survive Tutorial pt.1', student_id),
    ('How To Shoot Tutorial pt.1', student_id)
]
cursor.executemany(query, values)

# Создаем несколько учебных предметов (subjects)
query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.execute(query, ('Survival pt.1',))
subj1_id = cursor.lastrowid  # сохраняем id 1-го учебного предмета в переменную

cursor.execute(query, ('Shooting pt.1',))
subj2_id = cursor.lastrowid  # сохраняем id 2-го учебного предмета в переменную

cursor.execute(query, ('Martial Arts pt.1',))
subj3_id = cursor.lastrowid  # сохраняем id 3-го учебного предмета в переменную

# Создаем по два занятия для каждого предмета (lessons)
lesson_ids = []

query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
    ('Survival in the mountains Pro', subj1_id),
    ('Survival in urban environments Pro', subj1_id),
    ('Pistol Shooting Pro', subj2_id),
    ('Rifle Shooting Pro', subj2_id),
    ('Boxing Pro', subj3_id),
    ('Wrestling Pro', subj3_id)
]

for lesson in values:
    cursor.execute(query, lesson)
    lesson_ids.append(cursor.lastrowid)

# Определяем разные оценки для каждого урока
marks_values = [
    ('Excellent', lesson_ids[0], student_id),
    ('Good', lesson_ids[1], student_id),
    ('Satisfactory', lesson_ids[2], student_id),
    ('Good', lesson_ids[3], student_id),
    ('Excellent', lesson_ids[4], student_id),
    ('Satisfactory', lesson_ids[5], student_id)
]

# Выставляем нашему студенту оценки (marks) для всех созданных нами занятий
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(query, marks_values)

# Подтверждаем изменения в базе данных
db.commit()

# Получите информацию из базы данных:
# Все оценки студента
query = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query, (student_id,))
print("Все оценки студента:", cursor.fetchall())

# Все книги, которые находятся у студента
query = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query, (student_id,))
print("Все книги, которые находятся у студента:", cursor.fetchall())

# Для нашего студента выводим всё, что о нем есть в базе:
# группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
query = """
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    GROUP_CONCAT
        (DISTINCT b.title ORDER BY b.title SEPARATOR ', ') AS book_titles,
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
    subjects sub ON l.subject_id = sub.id
WHERE
    s.id = %s
GROUP BY
    s.name,
    s.second_name,
    g.title,
    sub.title,
    l.title,
    m.value
"""

cursor.execute(query, (student_id,))
student_info = cursor.fetchall()

# Выводим всю информацию о студенте
for info in student_info:
    print(info)


# Закрытие соединения с БД
cursor.close()
db.close()
