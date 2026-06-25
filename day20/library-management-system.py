class Book:
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            return "Borrowed successfully"
        else:
            return "Unavailable"
        
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            return "Book is available again"
        else:
            return "Book is already available"
        
    def show_info(self):
        status = "Available" if self.is_borrowed == False else "Unavailable"
        return f"{self.title} | {self.author} | {self.pages} | {status}"

books = [
    Book("Harry Potter", "J.K. Rowling", 450),
    Book("The Hobbit", "J.R.R. Tolkien", 310),
    Book("1984", "George Orwell", 280),
    Book("Animal Farm", "George Orwell", 120),
    Book("Dune", "Frank Herbert", 540),
    Book("The Alchemist", "Paulo Coelho", 180),
    Book("The Little Prince", "Antoine de Saint-Exupery", 110),
    Book("Sapiens", "Yuval Noah Harari", 500),
    Book("Atomic Habits", "James Clear", 320),
    Book("Clean Code", "Robert Martin", 460)
]
books[0].borrow()
books[1].return_book()
books[2].borrow()
books[3].borrow()
books[4].return_book()
books[5].borrow()
books[6].return_book()
books[7].borrow()
books[8].return_book()
books[9].return_book()


for book in books:
    print(book.show_info())

def borrowed_books(books):
    count = 0
    for book in books:
        if book.is_borrowed == True:
            count += 1
    return count
result = borrowed_books(books)
print("borrowed books=", result)

def available_books(books):
    count = 0
    for book in books:
        if book.is_borrowed == False:
            count += 1
    return count
result = available_books(books)
print("available books=", result)

def longest_book(books):
    longest_title = None
    longest_pages = -1
    for book in books:
        if book.pages > longest_pages:
            longest_pages = book.pages
            longest_title = book.title
    return longest_title, longest_pages
result = longest_book(books)
print(result)