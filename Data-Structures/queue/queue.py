class Queue:
    def __init__(self, max_size=128) -> None:
        self.queue = [0] * max_size
        self.max_size = max_size

        self.head = self.tail = -1
        self._size = 0

    def size(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self.size() == 0

    def peek(self) -> int:
        if self.isEmpty():
            raise RuntimeError("Queue is Empty!")
        return self.queue[self.head]

    def enqueue(self, val: int) -> None:
        if self.tail == self.max_size - 1:
            raise RuntimeError("Queue is Full!")
        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = val
        else:
            self.tail += 1
            self.queue[self.tail] = val

        self._size += 1

    def dequeue(self) -> int:
        if self.isEmpty():
            raise RuntimeError("Queue is Empty!")
        if self.size() == 1: # or `self.head == self.tail`
            val = self.queue[self.head]
            self.head = self.tail = -1
            self._size -= 1
            return val

        val = self.queue[self.head]
        self.head += 1
        self._size -= 1
        return val

    def printQueue(self) -> None:
        if self.isEmpty():
            print("Queue is Empty!")
            return

        for idx in range(self.head, self.tail + 1):
            print(self.queue[idx], end=" ")
        print()


if __name__ == "__main__":
    q = Queue()

    print("isEmpty():", q.isEmpty())
    q.print()

    print("\nenqueue(10)")
    q.enqueue(10)
    print("enqueue(20)")
    q.enqueue(20)
    print("enqueue(30)")
    q.enqueue(30)

    print("\nqueue: ", end="")
    q.printQueue()
    print("size():", q.size())

    print("\ndequeue():", q.dequeue())
    print("size():", q.size())
