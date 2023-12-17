from SymbolTable import SymbolTable
from queue import Queue

class Parser:

    def __init__(self, file_path):
        """
        Initializes an instance of Parser.

        Args:
            params:
                file_path:          .asm file.
        Vars:
            instance vars:
                symbol_table:        returns an instance of SymbolTable
                prepass:             returns a queue after file processing and removed of empty lines and comments
                ready_queue:         returns a another queue store label symbol into queue
        """
        self.symbol_table = SymbolTable()
        self.prepass = self.pre_process(file_path)
        self.ready_queue = self.label_process(self.prepass)

    #Remove empty lines and comments from the file
    #Store the lines into queue
    def pre_process(self, file_path):
        cleaned_code_queue = Queue()
        with open(file_path, 'r') as asm_file:
            for line in asm_file:
                newline = line = line.split('//')[0].strip()
                if line:
                    cleaned_code_queue.put(newline)
        return cleaned_code_queue

    #Add label symbol to the table with associated next line address
    #store every line of code in queue into another queue
    def label_process(self, queue):
        cleaned_code_queue = Queue()
        order = 0
        while not queue.empty():
            line = queue.get()
            if line.startswith('(') and line.endswith(')'):
                extracted = line[1:-1]
                if not self.symbol_table.contains(extracted):
                    self.symbol_table.add_label_entry(extracted, order)
            else:
                cleaned_code_queue.put(line)
                order += 1
        return cleaned_code_queue
    
    #print the queue
    def print_queue_contents(self, queue):
        while not queue.empty():
            print(queue.get())

    #parse comp
    def comp(self, c_instruction):
        equal_index = c_instruction.find('=')
        semicolon_index = c_instruction.find(';')

        if equal_index == 0 or semicolon_index == 0:
            raise ValueError("Invalid input. C instruction should only start with Letters or decimal")
        elif equal_index < 0 and semicolon_index < 0:
            raise ValueError("Invalid input. C instruction should contain either equal or semicolon")
        elif equal_index > 0 and semicolon_index > 0:
            return c_instruction[equal_index+1 :semicolon_index]
        elif equal_index > 0:
            return c_instruction[equal_index+1::]
        else:
            return c_instruction[:semicolon_index]
        
    #parse dest
    def dest(self, c_instruction):
        equal_index = c_instruction.find('=')
        if equal_index == 0:
            raise ValueError("Invalid input. C instruction should only start with Letters or decimal")
        elif equal_index > 0:
            return c_instruction[0:equal_index]
        else:
            return ''
        
    #parse jump
    def jump(self, c_instruction):
        semicolon_index = c_instruction.find(';')
        if semicolon_index < 0:
            return ''
        return c_instruction[semicolon_index+1::]

    #push symbol into table
    def push_symbol(self, symbol):
        self.symbol_table.add_entry(symbol)

