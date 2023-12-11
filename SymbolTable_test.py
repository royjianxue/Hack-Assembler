import unittest

from SymbolTable import SymbolTable  

class TestSymbolTable(unittest.TestCase):

    def setUp(self):
        # Initialize a SymbolTable instance for each test
        self.st = SymbolTable()

    def test_contains(self):
        self.assertTrue(self.st.contains('SP'))
        self.assertTrue(self.st.contains('R7'))
        self.assertFalse(self.st.contains('UNKNOWN'))

    def test_add_entry(self):
        self.st.add_entry('LOOP', 16)
        self.assertTrue(self.st.contains('LOOP'))
        self.assertEqual(self.st.retrive_address('LOOP'), 16)

    def test_retrieve_address(self):
        self.assertEqual(self.st.retrive_address('SCREEN'), 16384)
        self.assertIsNone(self.st.retrive_address('UNKNOWN'))

if __name__ == '__main__':
    unittest.main()
