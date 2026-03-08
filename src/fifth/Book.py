from __future__ import annotations


class Book:
    title: str | None = None
    author: str | None = None
    year: int | None = None

    def __init__(self, title: str = None, author: str = None, year: int = None) -> None:
        self.title = title
        self.author = author
        self.year = year

    def getinfo(self) -> None:
        print(f"Title: {self.title} Author: {self.author} Year: {self.year}")
