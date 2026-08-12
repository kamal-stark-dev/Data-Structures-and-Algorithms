import unittest

from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        """Runs before each individual test to set up a clean list."""
        self.st = Stack[int]()

    def test_add_and_size(self):
        self.assertTrue(self.st.isEmpty())

        self.st.push(10)
        self.st.push(20)
        self.st.push(30)

        self.assertEqual(self.st.size(), 3)
        self.assertEqual(self.st.peek(), 30)

    def test_pop_and_top(self):
        self.st.push(10)
        self.st.push(20)
        self.st.push(30)

        self.assertEqual(self.st.peek(), 30)
        self.assertEqual(self.st.pop(), 30)
        self.assertEqual(self.st.peek(), 20)

    def test_empty_stack_exceptions(self):
        with self.assertRaises(RuntimeError):
            self.st.peek()

        with self.assertRaises(RuntimeError):
            self.st.pop()

    def test_clear(self):
        self.st.push(1)
        self.st.push(2)

        self.st.clear()

        self.assertEqual(self.st.size(), 0)
        self.assertTrue(self.st.isEmpty())

    def test_push_after_clear(self):
        self.st.push(10)
        self.st.push(20)

        self.st.clear()

        self.st.push(30)

        self.assertEqual(self.st.size(), 1)
        self.assertEqual(self.st.peek(), 30)

    def test_string_stack(self):
        st = Stack[str]()

        st.push("Hello")
        st.push("World")

        self.assertEqual(st.peek(), "World")
        self.assertEqual(st.pop(), "World")
        self.assertEqual(st.peek(), "Hello")

    def test_float_stack(self):
        st = Stack[float]()

        st.push(1.5)
        st.push(2.5)
        st.push(3.5)

        self.assertEqual(st.peek(), 3.5)
        self.assertEqual(st.pop(), 3.5)
        self.assertEqual(st.size(), 2)



if __name__ == "__main__":
    unittest.main()