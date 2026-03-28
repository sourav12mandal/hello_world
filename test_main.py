import unittest
from main import get_greeting

class TestGreeting(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(get_greeting(), "Hello, World!")

    def test_custom_greeting(self):
        self.assertEqual(get_greeting("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
