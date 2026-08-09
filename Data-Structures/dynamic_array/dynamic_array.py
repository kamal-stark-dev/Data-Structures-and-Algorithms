"""
A dynamic array implementation in Python.

@author Kamalveer Singh, github.com/kamal-stark-dev
"""

class DynamicArray:
    def __init__(self, capacity = 16):
        if capacity < 0:
            raise ValueError("capacity can't be negative : /")

        self._size = 0
        self._capacity = max(capacity, 1)
        self._array = [None] * self._capacity


    # ----------------------
    #    Basic utilities
    # ----------------------

    def size(self):
        return self._size


    def is_empty(self):
        return self._size == 0


    def get(self, index):
        self._check_index(index)
        return self._array[index]


    def set(self, index, value):
        self._check_index(index)
        self._array[index] = value


    # ------------------------------
    #     Add (amortized O(1))
    # ------------------------------
    # Amortized: refers to the average time or resource cost of an operation over a long sequence of actions, rather than looking at any single execution in isolation.

    def add(self, value):
        if (self._size == self._capacity):
            self._resize(self._capacity * 2)

        self._array[self._size] = value
        self._size += 1


    # ------------------------------------------
    #     Remove ( O(n) shift, no rebuild )
    # ------------------------------------------

    def remove_at(self, index):
        self._check_index(index)

        removed_value = self._array[index]

        # shift left
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._array[self._size - 1] = None
        self._size -= 1

        # optional shrink (prevent waste of space)
        if 0 < self._capacity // 4 >= self._size:
            self._resize(self._capacity // 2)

        return removed_value


    def clear(self):
        self._array = [None] * self._capacity
        self._size = 0


    # -----------------------
    #    Internal Resize
    # -----------------------

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity


    # --------------------
    #     Index Check
    # -------------------

    def _check_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds : /")


    # ----------------------
    #     Print (clean)
    # ----------------------

    def __str__(self): # `__str__` dunder method defines how this object should look when printed (Usage: `print(obj)`)
        return "[" + ", ".join(str(self._array[i]) for i in range(self._size)) + "]"

    def __repr__(self):
        return f"DynamicArray(size={self._size}, capacity={self._capacity})"

arr = DynamicArray(1)

arr.add(3.14)
arr.add(10)
arr.add("Jake")

print(arr)             # [10, 20, 30]
print(repr(arr))

arr.set(1, 69)
print(arr)             # [10, 69, 30]

arr.remove_at(1)
print(arr)             # [10, 30]

print(arr.size())      # 2
print(arr.is_empty())  # False

arr.clear()
print(arr)             # []