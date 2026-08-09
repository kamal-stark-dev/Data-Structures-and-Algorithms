class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __iter__(self):
        """Allows iterating through the linked list using a for loop."""
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def clear(self):
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = curr.prev = None
            curr.val = 0
            curr = next_node
        self.head = self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self.size() == 0

    def addFirst(self, val):
        if self.isEmpty():
            self.head = self.tail = ListNode(val)
        else:
            node = ListNode(val, next=self.head)
            self.head.prev = node
            self.head = node
        self._size += 1

    def addLast(self, val):
        if self.isEmpty():
            self.head = self.tail = ListNode(val)
        else:
            node = ListNode(val, prev=self.tail)
            self.tail.next = node
            self.tail = node
        self._size += 1

    def peekFirst(self):
        if self.isEmpty():
            raise RuntimeError("List is empty!!")
        return self.head.val

    def peekLast(self):
        if self.isEmpty():
            raise RuntimeError("List is empty!!")
        return self.tail.val

    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("List is empty!!")

        data = self.head.val
        self.head = self.head.next

        if not self.head:
            self.tail = None
        else:
            self.head.prev = None

        self._size -= 1
        return data

    def removeLast(self):
        if self.isEmpty():
            raise RuntimeError("List is empty!!")

        data = self.tail.val
        self.tail = self.tail.prev

        if not self.tail:
            self.head = None
        else:
            self.tail.next = None

        self._size -= 1
        return data

    def _remove(self, node):
        if not node.prev:
            return self.removeFirst()
        if not node.next:
            return self.removeLast()

        # make pointers of adjacent nodes skip the current node
        node.prev.next = node.next
        node.next.prev = node.prev

        data = node.val

        node.val = 0
        node.prev = node.next = None

        self._size -= 1
        return data

    def remove(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                self._remove(curr)
                return True
            curr = curr.next

        return False

    def removeAt(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range!!")

        if idx < (self._size // 2):
            # search from the start of the list
            curr = self.head
            i = 0
            while i != idx:
                curr = curr.next
                i += 1

        else:
            # start from the end of the list
            curr = self.tail
            i = self._size - 1
            while i != idx:
                curr = curr.prev
                i -= 1

        return self._remove(curr)

    def insertAt(self, idx, val):
        if idx < 0 or idx > self._size:
            raise IndexError("Invalid range provided!!")

        if idx == 0:
            self.addFirst(val)
            return
        if idx == self._size:
            self.addLast(val)
            return

        if idx < (self._size // 2):
            curr = self.head
            i = 0
            while i != idx - 1:
                curr = curr.next
                i += 1
        else:
            curr = self.tail
            i = self._size - 1
            while i != idx - 1:
                curr = curr.prev
                i -= 1

        node = ListNode(val, prev=curr, next=curr.next)
        curr.next.prev = node
        curr.next = node

        self._size += 1

    def indexOf(self, val):
        curr = self.head
        i = 0
        while curr:
            if curr.val == val:
                return i
            i += 1
            curr = curr.next

        return -1

    def contains(self, val):
        return self.indexOf(val) != -1

    def printList(self):
        curr = self.head

        if not curr:
            print("List is empty!!")
            return

        print("List: NULL <-> ", end="")
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("NULL")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.addFirst(1) # [1]
    dll.addFirst(2) # [2, 1]
    dll.addLast(3) # [2, 1, 3]

    dll.printList() # NULL <-> 2 <-> 1 <-> 3 <-> NULL
    print("Size:", dll.size()) # 3

    print("Index of 1:", dll.indexOf(1)) # 0

    dll.removeLast() # [2, 1]
    dll.printList()

    print("Contains 2: ", dll.contains(2))

    dll.removeFirst() # [1]
    dll.printList()

    dll.remove(1) # []
    dll.printList()
    print("Size:", dll.size()) # 3