-- Создаем группу (group)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('The Killers', 'may 2024', 'aug 2024')

-- Создаем студента (student) и определяем его в группу
INSERT INTO students (name, second_name, group_id) VALUES ('John', 'Wick', 1238)

-- Создаем несколько книг (books) и указываем, что наш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('How To Survive Tutorial', 1289)

INSERT INTO books (title, taken_by_student_id) VALUES ('How To Shoot Tutorial', 1289)

-- Создаем несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Survival')

INSERT INTO subjets (title) VALUES ('Shooting')

INSERT INTO subjets (title) VALUES ('Martial Arts')

-- Создаем по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('Survival in the mountains', 1702)

INSERT INTO lessons (title, subject_id) VALUES ('Survival in urban environments', 1702)

INSERT INTO lessons (title, subject_id) VALUES ('Pistol Shooting', 1703)

INSERT INTO lessons (title, subject_id) VALUES ('Rifle Shooting', 1703)

INSERT INTO lessons (title, subject_id) VALUES ('Boxing', 1704)

INSERT INTO lessons (title, subject_id) VALUES ('Wrestling', 1704)

-- Выставляем нашему студенту оценки (marks) для всех созданных нами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3986, 1289)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3987, 1289)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3988, 1289)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3989, 1289)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3990, 1289)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('Excellent', 3991, 1289)


-- Получите информацию из базы данных:
-- Все оценки студента
SELECT value FROM marks WHERE student_id = 1289

-- Все книги, которые находятся у студента
SELECT title FROM books WHERE taken_by_student_id = 1289

-- Для студента выведите всё, что о нем есть в базе:
-- группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
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
    s.id = 1289


-- ниже представлено решение для более красивого отображения таблицы.
-- P.S. тут мне помог ChatGPT, т.к. я не был в курсе групповой агрегации данных.

SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    GROUP_CONCAT(DISTINCT b.title ORDER BY b.title SEPARATOR ', ') AS book_titles,
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
    s.id = 1289
GROUP BY
    s.name,
    s.second_name,
    g.title,
    sub.title,
    l.title,
    m.value;
