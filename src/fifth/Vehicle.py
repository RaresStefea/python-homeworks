from __future__ import annotations


class Vehicle:
    brand: str | None = None
    year: int | None = None

    def __init__(self, brand: str = None, year: int = None) -> None:
        self.brand = brand
        self.year = year

    def display_info(self) -> None:
        print(f"Brand: {self.brand} Year: {self.year}", end=" ")
