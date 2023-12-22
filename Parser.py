from SymbolTable import SymbolTable
from queue import Queue

class Parser:
    """
    Class for parsing Hack assembly code.

    Attributes:
        symbol_table (SymbolTable): An instance of the SymbolTable class.
        prepass (Queue): A queue containing the pre-processed assembly code.
        ready_queue (Queue): A queue containing the processed assembly code with labels and removed empty lines.
    """

    def __init__(self, file_path):
        """
        Initializes an instance of Parser.

        Args:
            file_path (str): Path to the .asm file.

        Attributes:
            symbol_table (SymbolTable): Instance of SymbolTable class.
            prepass (Queue): Queue after file processing, removed of empty lines and comments.
            ready_queue (Queue): Another queue storing label symbols after processing.
        """
        self.symbol_table = SymbolTable()
        self.prepass = self.pre_process(file_path)
        self.ready_queue = self.label_process(self.prepass)

    def pre_process(self, file_path):
        """
        Removes empty lines and comments from the file and stores the lines into a queue.

        Args:
            file_path (str): Path to the .asm file.

        Returns:
            Queue: Queue containing the cleaned lines of code.
        """
        cleaned_code_queue = Queue()
        with open(file_path, 'r') as asm_file:
            for line in asm_file:
                newline = line.split('//')[0].strip()
                if newline:
                    cleaned_code_queue.put(newline)
        return cleaned_code_queue


    def label_process(self, queue):
        """
        Adds label symbols to the table with associated next line addresses.
        Stores every line of code in the queue into another queue.

        Args:
            queue (Queue): Queue containing the pre-processed lines of code.

        Returns:
            Queue: Queue containing processed lines of code with labels removed.
        """
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
 
    def comp(self, c_instruction):
        """
        Parses the comp part of a C-instruction.

        Args:
            c_instruction (str): The C-instruction.

        Returns:
            str: The parsed comp part of the C-instruction.

        Raises:
            ValueError: If the C-instruction is invalid.
        """
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
        

    def dest(self, c_instruction):
        """
        Parses the dest part of a C-instruction.

        Args:
            c_instruction (str): The C-instruction.

        Returns:
            str: The parsed dest part of the C-instruction.

        Raises:
            ValueError: If the C-instruction is invalid.
        """
        equal_index = c_instruction.find('=')
        if equal_index == 0:
            raise ValueError("Invalid input. C instruction should only start with Letters or decimal")
        elif equal_index > 0:
            return c_instruction[0:equal_index]
        else:
            return ''
        
 
    def jump(self, c_instruction):
        """
        Parses the jump part of a C-instruction.

        Args:
            c_instruction (str): The C-instruction.

        Returns:
            str: The parsed jump part of the C-instruction.

        Raises:
            ValueError: If the C-instruction is invalid.
        """
        semicolon_index = c_instruction.find(';')
        if semicolon_index < 0:
            return ''
        return c_instruction[semicolon_index+1::]

    def push_symbol(self, symbol):
        """
        Pushes a symbol into the symbol table.

        Args:
            symbol (str): The symbol to be pushed into the symbol table.
        """
        self.symbol_table.add_entry(symbol)

