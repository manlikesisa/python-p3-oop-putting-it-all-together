#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None  # Starts unset

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
