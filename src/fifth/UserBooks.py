from __future__ import annotations

"""
Implement three classes (Users, Books, UserBooks) that interact with our DB module
1. Users class with functions (add, list, get, delete) using our DB module
2. Books class with same functions
3. UserBooks class with functions:
a. add_bookid_user, id_book) - Assigns a book to a user
b. get_books (id_user) - Returns a list of book details (not just IDs)
C.
has_read_bookid_user, id_book) - Returns True/False if a user has read a book.
Improvements:
Prevent duplicate entries (a user shouldn't have the same book added twice).
Add a function remove_book(user_id, book_id) to allow users to return
"""
