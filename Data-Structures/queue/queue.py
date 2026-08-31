class Queue:
    def __init__(self, max_size=128) -> None:
        if max_size <= 0:
            raise ValueError("max_size must be greater than 0")
        self.max_size = max_size
        self.queue = [0] * max_size

        self.head = self.tail = -1
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def is_full(self) -> bool:
        return self._size == self.max_size

    def peek(self) -> int:
        if self.is_empty():
            raise RuntimeError("Queue is Empty!")
        return self.queue[self.head]

    def enqueue(self, val: int) -> None:
        if self.is_full():
            raise RuntimeError("Queue is Full!")
        if self.is_empty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = val
        else:
            self.tail += 1
            self.queue[self.tail] = val

        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise RuntimeError("Queue is Empty!")
        if self.head == self.tail:
            val = self.queue[self.head]
            self.head = self.tail = -1
            self._size -= 1
            return val

        val = self.queue[self.head]
        self.head += 1
        self._size -= 1
        return val

    def print_queue(self) -> None:
        if self.is_empty():
            print("Queue is Empty!")
            return

        print("head -> [", end="")
        for idx in range(self.head, self.tail + 1):
            print(self.queue[idx], end=", ")
        print("\b\b] <- tail")


if __name__ == "__main__":
    q = Queue(8)

    print("is_empty():", q.is_empty())
    q.print_queue()

    print("\nenqueue(10)")
    q.enqueue(10)
    print("enqueue(20)")
    q.enqueue(20)
    print("enqueue(30)")
    q.enqueue(30)

    print("\nqueue: ", end="")
    q.print_queue()
    print("size():", q.size())

    print("\ndequeue():", q.dequeue())
    print("size():", q.size())
