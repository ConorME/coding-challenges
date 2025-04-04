import unittest

class b_Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimal_tree(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = b_Node(value=arr[mid])
    root.left = minimal_tree(arr, start, mid - 1)
    root.right = minimal_tree(arr, mid + 1, end)
    return root

class MinimalTreeTest(unittest.TestCase):
    def setUp(self):
        self.arr_odd      = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.arr_even     = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.arr_small    = [0, 1]
        self.arr_one      = [0]
        self.arr_empty    = []
        self.arr_small_odd= [0, 1, 2]

    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

    def test_empty(self):
        root = minimal_tree(self.arr_empty, 0, len(self.arr_empty) - 1)
        self.assertIsNone(root, "An empty array should produce a None tree.")

    def test_one(self):
        root = minimal_tree(self.arr_one, 0, len(self.arr_one) - 1)
        self.assertIsNotNone(root, "A single-element array should produce a node.")
        self.assertEqual(root.value, 0)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_small(self):
        # For [0, 1]: mid = (0+1)//2 = 0, so root should be 0 with right child 1.
        root = minimal_tree(self.arr_small, 0, len(self.arr_small) - 1)
        self.assertIsNotNone(root)
        self.assertEqual(root.value, 0)
        self.assertIsNone(root.left)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.value, 1)

    def test_small_odd(self):
        # For [0, 1, 2]: mid = (0+2)//2 = 1, so root should be 1, with left 0 and right 2.
        root = minimal_tree(self.arr_small_odd, 0, len(self.arr_small_odd) - 1)
        self.assertIsNotNone(root)
        self.assertEqual(root.value, 1)
        self.assertIsNotNone(root.left)
        self.assertEqual(root.left.value, 0)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.value, 2)

    def test_odd(self):
        # For an odd-length array, an in-order traversal of the minimal tree
        # should yield the original array.
        root = minimal_tree(self.arr_odd, 0, len(self.arr_odd) - 1)
        self.assertEqual(self.inorder(root), self.arr_odd)

    def test_even(self):
        # For an even-length array, an in-order traversal should still yield the original array.
        root = minimal_tree(self.arr_even, 0, len(self.arr_even) - 1)
        self.assertEqual(self.inorder(root), self.arr_even)

if __name__ == '__main__':
    unittest.main()
   
