from SymbolTable import SymbolTable
from LabelTable import LabelTable
from queue import Queue

class Parser:

    comp_codes = {
    '0':   '0101010',
    '1':   '0111111',
    '-1':  '0111010',
    'D':   '0001100',
    'A':   '0110000',
    'M':   '1110000',
    '!D':  '0001101',
    '!A':  '0110001',
    '!M':  '1110001',
    '-D':  '0001111',
    '-A':  '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'M+1': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'D+M': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'D&M': '1000000',
    'D|A': '0010101',
    'D|M': '1010101'
}

    dest_codes = {
    'null': '000',
    'M':    '001',
    'D':    '010',
    'MD':   '011',
    'A':    '100',
    'AM':   '101',
    'AD':   '110',
    'AMD':  '111'
}

    jump_codes = {
    'null': '000',
    'JGT':  '001',
    'JEQ':  '010',
    'JGE':  '011',
    'JLT':  '100',
    'JNE':  '101',
    'JLE':  '110',
    'JMP':  '111'
}

    def __init__(self, file_path):
        self.symbol_table = SymbolTable()
        self.label_table = LabelTable()
        self.prepass = self.pre_pass(file_path)
        self.firstpass = self.first_pass(self.prepass)
    
    #Remove empty lines, and comment lines //
    def pre_pass(self, file_path):
        cleaned_code_queue = Queue()
        with open(file_path, 'r') as asm_file:
            for line in asm_file:
                newline = line = line.split('//')[0].strip()
                if line:
                    cleaned_code_queue.put(newline)
        return cleaned_code_queue

    #Add label symbol to the table
    def first_pass(self, queue):
        cleaned_code_queue = Queue()
        order = 0
        while not queue.empty():
            line = queue.get()
            if line.startswith('(') and line.endswith(')'):
                extracted = line[1:-1]
                if not self.label_table.contains(extracted):
                    self.label_table.add_entry(extracted, order)
            else:
                cleaned_code_queue.put(line)
                order += 1
        return cleaned_code_queue


    def print_queue_contents(self, queue):
        while not queue.empty():
            print(queue.get())

    #parsing decimal
    def parse_a_instruction_immediate_value(self, instruction):
        return self.decimal_to_16bit(instruction)
    
    #parsing variable
    def parse_a_instruction_variable(self, instruction):



        pass
    
    def parse_c_instruction(self, instruction):
        pass

    def parse_L_instruction(self, instruction):
        pass

    #convert string decimal into 16bit string binary value
    def decimal_to_16bit(self, decimal_value_str):
        try:
            decimal_value = int(decimal_value_str)
        except ValueError:
            raise ValueError("Invalid decimal value: {}".format(decimal_value_str))
        
        binary_string = format(decimal_value, '016b')
        
        return binary_string
    #function check to see if symbol is contained in the table already
    def is_in_symbol_table(self, symbol):
        return self.symbol_table.contains(symbol)
    
