# Write a program which can store books in a library.
# Every library has a name and can store multiple books.
# Every book has a title, an author, a release year and a weight.
# The library must provide the following functionalities:
# We can add books to the library
# We want to be able to remove a book by title
# We also want to be able to get the books that were released in a given year
# We also want to be able to get the lightest book



class Book:
    def __init__(self, title, author, release_year, weight):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.weight = weight


class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def add(self, title):
        self.book_list.append(title)

    def remove(self, book_title):
        book_to_remove = None
        for i in self.book_list:
            if book_title == i.title:
                book_to_remove = i
        self.book_list.remove(book_to_remove)

    def get_books_by_year(self, year):
        result = []
        for index, book in enumerate(self.book_list):
            if book.release_year == year:
                result.append(book)
        return result

    def get_lightest(self):
        try:
            lightest = self.book_list[0]
            for i in self.book_list:
                if lightest.weight > i.weight:
                    lightest = i
            return lightest.title
        except IndexError:

            print("There are no books in the library! :(")




library = Library("City Central")
library.get_lightest()
book1 = Book("Life of A", "A", 2000, 8)
library.add(book1)
# print(type(book1.year))
library.add(Book("Life of B", "B", 2000, 10))
library.add(Book("Life of C", "C", 2001, 12))
library.add(Book("Life of D", "D", 2002, 16))
print(len(library.get_books_by_year(2000)))  # should print: 2
print(library.get_lightest())  # should print: Life of A
library.remove("Life of A")
library.add(Book("Life of D", "D", 2002, 2))
print(len(library.get_books_by_year(2000)))  # should print: 1
print(library.get_lightest())  # should print: Life of D







