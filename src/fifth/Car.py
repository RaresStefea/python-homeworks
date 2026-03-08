from __future__ import annotations
from .Vehicle import Vehicle
from .Fuel import Fuel


class Car(Vehicle):
    fuel_type: Fuel | None = None

    def __init__(self, brand: str = None, year: int = None, fuel_type: Fuel = None):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type.value if self.fuel_type else None}")
