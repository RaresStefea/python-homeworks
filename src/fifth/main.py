from .Book import Book
from .Car import Car
from .Fuel import Fuel
from .db import init_db
from .Users import Users
from .Books2 import Books
from .UserBooks import UserBooks

first_book = Book("1984", "George Orwell", 1949)
second_book = Book("To Kill A Mockingbird", "Harper Lee", 1960)
third_book = Book()

first_book.getinfo()
second_book.getinfo()
third_book.getinfo()

first_car = Car("Toyota", 1984, Fuel.PETROL)
second_car = Car()

first_car.display_info()
second_car.display_info()

print("Input the file path:")
db_path = input().strip()
init_db(db_path)

users = Users(db_path)
books = Books(db_path)
user_books = UserBooks(db_path)

users.add("Alice")
users.add("Bob")

books.add("1984", "George Orwell", 1949)
books.add("To Kill A Mockingbird", "Harper Lee", 1960)
books.add("Dune", "Frank Herbert", 1965)

print("All users:")
users.list()

print("All books:")
books.list()

user_books.add_book(1, 1)
user_books.add_book(1, 2)
user_books.add_book(2, 3)
user_books.add_book(1, 1)  # duplicate

print("Books read by 1:")
print(user_books.get_books(1))

print("Has 1 read 1", user_books.has_read(1, 1))
print("Has 1 read 3", user_books.has_read(1, 3))

user_books.remove_book(1, 2)
print("Removed book:")
print(user_books.get_books(1))
