import unittest
from Stack import Stack, EmptyStackError
from MinStack import MinStack

class TestStack(unittest.TestCase):
    def test_push_and_peek(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)

    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        with self.assertRaises(EmptyStackError):
            stack.pop()

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        self.assertFalse(stack.is_empty())

class TestMinStack(unittest.TestCase):
    def test_min(self):
        min_stack = MinStack()
        min_stack.push(10)
        self.assertEqual(min_stack.min(), 10)
        min_stack.push(5)
        self.assertEqual(min_stack.min(), 5)
        min_stack.push(15)
        self.assertEqual(min_stack.min(), 5)

    def test_min_on_empty_stack(self):
        min_stack = MinStack()
        self.assertIsNone(min_stack.min()) 

    def test_min_with_pop(self):
        min_stack = MinStack()
        min_stack.push(10)
        min_stack.push(5)
        min_stack.push(15)
        min_stack.pop()
        self.assertEqual(min_stack.min(), 5)
        min_stack.pop()
        self.assertEqual(min_stack.min(), 10)

    def test_push_and_pop(self):
        min_stack = MinStack()
        min_stack.push(10)
        min_stack.push(20)
        self.assertEqual(min_stack.pop(), 20)
        self.assertEqual(min_stack.pop(), 10)
        with self.assertRaises(EmptyStackError):
            min_stack.pop()

if __name__ == "__main__":
    unittest.main()

