from typing import Generic, TypeVar
from doubly_list import DoublyLinkedList

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.list: DoublyLinkedList = DoublyLinkedList()
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self.size() == 0

    def push(self, val: T) -> None:
        self.list.addLast(val)
        self._size += 1

    def peek(self) -> T:
        if self.isEmpty():
            raise RuntimeError("Stack is empty!!")
        return self.list.tail.val

    def pop(self) -> T:
        if self.isEmpty():
            raise RuntimeError("Stack is empty!!")
        val: T = self.list.tail.val
        self.list.removeLast()
        self._size -= 1
        return val

    def clear(self) -> None:
        while not self.isEmpty():
            self.pop()

if __name__ == "__main__":
    st = Stack[int]()

    print("isEmpty:", st.isEmpty())

    print("\nPushing Values:")
    print("\nPush 10")
    st.push(10)

    print("Push 20")
    st.push(20)

    print("Push 30")
    st.push(30)

    print("\nTop:", st.peek())
    print("Pop:", st.pop())

    print("\nTop:", st.peek())
    print("Size:", st.size())

    st.clear()
    print("\nClearing Stack")
    print("Size:", st.size())