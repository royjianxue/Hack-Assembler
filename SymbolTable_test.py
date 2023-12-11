import unittest
from SymbolTable import SymbolTable  #import the SymbolTable class from SymbolTable module

class TestSymbolTable(unittest.TestCase):

    def setUp(self):
        # Initialize a SymbolTable instance for each test
        self.symbol_table = SymbolTable()

    def test_contains(self):
        self.assertTrue(self.symbol_table.contains('SP'))
        self.assertTrue(self.symbol_table.contains('R7'))
        self.assertFalse(self.symbol_table.contains('UNKNOWN'))

    def test_add_entry(self):
        self.symbol_table.add_entry('LOOP', 16)
        self.assertTrue(self.symbol_table.contains('LOOP'))
        self.assertEqual(self.symbol_table.retrive_address('LOOP'), 16)

    def test_retrieve_address(self):
        self.assertEqual(self.symbol_table.retrive_address('SCREEN'), 16384)
        self.assertIsNone(self.symbol_table.retrive_address('UNKNOWN'))

if __name__ == '__main__':
    unittest.main()
