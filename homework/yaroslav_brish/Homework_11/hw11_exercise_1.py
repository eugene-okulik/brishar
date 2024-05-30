class Book:
    pages_material = 'бумага'
    has_text = True

    def __init__(self, title, author, page_count, isbn):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = False  # Атрибут зарезервированности, по умолчанию False

    def reserve(self):  # Метод для резервирования книги
        self.is_reserved = True

    def get_book_details(self):  # Метод для вывода деталей книги
        reservation_status = ", зарезервирована" if self.is_reserved else ""

        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                f"материал: {Book.pages_material}{reservation_status}")


class SchoolBook(Book):
    def __init__(self, title, author, page_count, isbn, subject, grade, has_exercises):
        super().__init__(title, author, page_count, isbn)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def get_book_details(self):  # Метод для вывода деталей учебника
        reservation_status = ", зарезервирована" if self.is_reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                f"предмет: {self.subject}, класс: {self.grade}{reservation_status}")


# Задание №1
book_1 = Book('Идиот', 'Достоевский', 500, 9780394604343)
book_2 = Book('Преступление и наказание', 'Достоевский', 492, 9788420741468)
book_3 = Book('Три товарища', 'Ремарк', 498, 9780449912423)
book_4 = Book('Анна Каренина', 'Толстой', 864, 9780679410003)
book_5 = Book('1984', 'Оруэлл', 328, 9780436350221)

# Помечаем одну книгу как зарезервированную
book_3.reserve()

# Печать деталей о каждой книге
books = [book_1, book_2, book_3, book_4, book_5]
for book in books:
    print(book.get_book_details())


# Задание №2
school_book1 = SchoolBook('Алгебра', 'Иванов', 200,
                          9785170822953, 'Математика', 9, True)
school_book2 = SchoolBook('История', 'Петров', 300,
                          9785170832594, 'История', 10, True)
school_book3 = SchoolBook('География', 'Сидоров', 250,
                          9785389073305, 'География', 8, False)
school_book4 = SchoolBook('Физика', 'Кузнецов', 280,
                          9785171183663, 'Физика', 11, True)
school_book5 = SchoolBook('Биология', 'Васильев', 230,
                          9785171041826, 'Биология', 7, True)

# Помечаем один учебник как зарезервированный
school_book1.reserve()

# Печать деталей о каждом учебнике
school_books = [school_book1, school_book2, school_book3, school_book4, school_book5]
for book in school_books:
    print(book.get_book_details())
