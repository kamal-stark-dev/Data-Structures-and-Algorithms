import unittest
# python -m unittest test_dll.py

# Assuming your DoublyLinkedList class is in a file named dll.py
from doubly_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        """Runs before each individual test to set up a clean list."""
        self.dll = DoublyLinkedList()

    def test_add_and_size(self):
        self.assertTrue(self.dll.isEmpty())
        self.dll.addFirst(10)
        self.dll.addLast(20)
        self.dll.addFirst(5)

        # Current structure: [5, 10, 20]
        self.assertEqual(self.dll.size(), 3)
        self.assertEqual(self.dll.peekFirst(), 5)
        self.assertEqual(self.dll.peekLast(), 20)

    def test_remove_first_and_last(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.dll.addLast(3)

        self.assertEqual(self.dll.removeFirst(), 1)
        self.assertEqual(self.dll.removeLast(), 3)
        self.assertEqual(self.dll.size(), 1)
        self.assertEqual(self.dll.peekFirst(), 2)

    def test_remove_by_value(self):
        self.dll.addLast(10)
        self.dll.addLast(20)
        self.dll.addLast(30)

        self.assertTrue(self.dll.remove(20))
        self.assertFalse(self.dll.remove(99))  # Non-existent value
        self.assertEqual(self.dll.size(), 2)
        self.assertEqual(self.dll.indexOf(30), 1)

    def test_remove_at_index(self):
        self.dll.addLast(10) # Index 0
        self.dll.addLast(20) # Index 1
        self.dll.addLast(30) # Index 2
        self.dll.addLast(40) # Index 3

        # Test removing from the second half (utilizes tail search optimization)
        self.assertEqual(self.dll.removeAt(2), 30)
        # Test removing from the first half (utilizes head search)
        self.assertEqual(self.dll.removeAt(0), 10)

        self.assertEqual(self.dll.size(), 2)

        # Out of bounds should raise IndexError
        with self.assertRaises(IndexError):
            self.dll.removeAt(5)

    def test_empty_list_exceptions(self):
        with self.assertRaises(RuntimeError):
            self.dll.peekFirst()
        with self.assertRaises(RuntimeError):
            self.dll.removeLast()

    def test_iterator(self):
        items = [1, 2, 3, 4]
        for item in items:
            self.dll.addLast(item)

        # Convert iterator directly to a python list to verify elements
        self.assertEqual(list(self.dll), items)

        # Verify a standard manual loop functions perfectly
        loop_elements = []
        for val in self.dll:
            loop_elements.append(val)
        self.assertEqual(loop_elements, items)

    def test_insert_at_index(self):
        self.dll.addLast(10) # [10]
        self.dll.addLast(30) # [10, 30]

        # Test inserting in the middle
        self.dll.insertAt(1, 20) # [10, 20, 30]
        self.assertEqual(list(self.dll), [10, 20, 30])

        # Test inserting at 0-th index
        self.dll.insertAt(0, 0) # [0, 10, 20, 30]
        self.assertEqual(self.dll.peekFirst(), 0)

        # Test inserting at the absolute end (idx == size)
        self.dll.insertAt(4, 40) # [0, 10, 20, 30, 40]
        self.assertEqual(self.dll.peekLast(), 40)

        # Test out of bounds
        with self.assertRaises(IndexError):
            self.dll.insertAt(10, 99)

    def test_reverse_list(self):
        # Case 1: Empty list should not crash
        self.dll.reverseList()
        self.assertTrue(self.dll.isEmpty())

        # Case 2: Multi-element list
        self.dll.addLast(10)
        self.dll.addLast(20)
        self.dll.addLast(30)

        self.dll.reverseList()

        # Verify structure forward
        self.assertEqual(list(self.dll), [30, 20, 10])
        # Verify head and tail references updated correctly
        self.assertEqual(self.dll.peekFirst(), 30)
        self.assertEqual(self.dll.peekLast(), 10)

    def test_clear(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.dll.clear()
        self.assertEqual(self.dll.size(), 0)
        self.assertTrue(self.dll.isEmpty())

if __name__ == "__main__":
    unittest.main()