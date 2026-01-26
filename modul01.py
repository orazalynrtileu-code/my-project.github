class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' | {self.author} (ISBN: {self.isbn}, Қолда бар: {self.copies})"


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []  

    def __str__(self):
        return f"Оқырман: {self.name} (ID: {self.reader_id})"


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    
    def add_book(self, book):
        self.books.append(book)
        print(f"Кітап қосылды: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Кітап өшірілді: {book.title}")
                return
        print("Кітап табылмады!")

    
    def register_reader(self, reader):
        self.readers.append(reader)
        print(f"Жаңа оқырман тіркелді: {reader.name}")

    def remove_reader(self, reader_id):
        for reader in self.readers:
            if reader.reader_id == reader_id:
                self.readers.remove(reader)
                print(f"Оқырман өшірілді: {reader.name}")
                return
        print("Оқырман табылмады!")

    
    def issue_book(self, reader_id, isbn):
        
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if reader and book:
            if book.copies > 0:
                book.copies -= 1
                reader.borrowed_books.append(book)
                print(f"Кітап берілді: {book.title} -> {reader.name}")
            else:
                print(f"Кешіріңіз, '{book.title}' кітабы таусылды.")
        else:
            print("Оқырман немесе кітап табылмады!")

    def return_book(self, reader_id, isbn):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        if reader:
            for book in reader.borrowed_books:
                if book.isbn == isbn:
                    book.copies += 1
                    reader.borrowed_books.remove(book)
                    print(f"Кітап қайтарылды: {book.title} <- {reader.name}")
                    return
        print("Қайтару қатесі: деректерді тексеріңіз.")




my_library = Library()


book1 = Book("Абай жолы", "Мұхтар Әуезов", "978-01", 3)
book2 = Book("Қан мен тер", "Әбдіжәміл Нұрпейісов", "978-02", 1)
reader1 = Reader("Әлихан", "ID001")
reader2 = Reader("Айжан", "ID002")

print("--- Тіркеу және Қосу ---")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.register_reader(reader1)
my_library.register_reader(reader2)

print("\n--- Кітап беру процесі ---")
my_library.issue_book("ID001", "978-01")
my_library.issue_book("ID002", "978-02") 
my_library.issue_book("ID001", "978-02") 

print("\n--- Күйді тексеру ---")
print(book1) 
print(book2) 

print("\n--- Қайтару және өшіру ---")
my_library.return_book("ID001", "978-01")
my_library.remove_book("978-02")