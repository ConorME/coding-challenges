import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=10)
        self.ht.insert("key1", "value1")
        self.ht.insert("key2", "value2")
        self.ht.insert("key3", "value3")

    def test_insert(self):
        self.ht.insert("key4", "value4")
        self.assertEqual(self.ht.get("key4"), "value4")
        self.ht.insert("key1", "new_value1")
        self.assertEqual(self.ht.get("key1"), "new_value1")

    def test_get(self):
        self.assertEqual(self.ht.get("key1"), "value1")
        self.assertEqual(self.ht.get("key2"), "value2")
        self.assertIsNone(self.ht.get("key4")) 

    def test_remove(self):
        self.assertTrue(self.ht.remove("key2"))
        self.assertIsNone(self.ht.get("key2"))
        self.assertFalse(self.ht.remove("key4"))
    
    def test_collision_handling(self):
        key1_index = self.ht._hash("key1")
        key4 = f"key1_collision_{key1_index}" 
        self.ht.insert(key4, "collision_value")
        self.assertEqual(self.ht.get(key4), "collision_value")
        self.assertEqual(self.ht.get("key1"), "value1")

    def test_string_representation(self):
        self.assertIsInstance(str(self.ht), str)

if __name__ == "__main__":
    unittest.main()

