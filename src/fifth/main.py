from .Book import Book
from .Car import Car
from .Fuel import Fuel

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
