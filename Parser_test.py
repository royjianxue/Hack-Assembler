import unittest
from Parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        # Initialize a Parser instance for each test
        self.parser = Parser()


    def test_immediate_value_conversion(self):

        self.assertEqual(self.parser.decimal_to_16bit('42'), '0000000000101010')
        self.assertEqual(self.parser.decimal_to_16bit('23'), '0000000000010111')
        self.assertEqual(self.parser.decimal_to_16bit('1'), '0000000000000001')
        self.assertEqual(self.parser.decimal_to_16bit('0'), '0000000000000000')
        self.assertEqual(self.parser.parse_a_instruction_immediate_value('42'), '0000000000101010')
        self.assertEqual(self.parser.parse_a_instruction_immediate_value('23'), '0000000000010111')
        self.assertEqual(self.parser.parse_a_instruction_immediate_value('1'), '0000000000000001')
        self.assertEqual(self.parser.parse_a_instruction_immediate_value('0'), '0000000000000000')

    def test_is_in_symbol_table(self):
        self.assertTrue(self.parser.is_in_symbol_table('R0'))
        self.assertTrue(self.parser.is_in_symbol_table('LCL'))
        self.assertTrue(self.parser.is_in_symbol_table('SCREEN'))
        self.assertFalse(self.parser.is_in_symbol_table('AB'))
        self.assertFalse(self.parser.is_in_symbol_table('CD'))


    
if __name__ == '__main__':
    unittest.main()
