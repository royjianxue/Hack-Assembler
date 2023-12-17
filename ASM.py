from Parser import Parser
from Code import Code
import argparse


def a_instruction(queue, parser):
    """
    Processes an A-instruction from the queue.

    Args:
        queue(str): A string representing the queue of A-instructions.
        parser(obj): parser object to call its methods

    Returns:
        str: The decimal representation of the A-instruction.

    Raises:
        ValueError: If the A-instruction is invalid.
    """
    
    # Extract the A-instruction from the queue, removing '@' from the begining
    line = queue[1::]

    # Check if the A-instruction is a decimal value
    if line.isdigit():
        return Code.compute_decimal_instruction(line)
    
    # Check if the A-instruction is a symbol starting with an integer
    elif not line.isdigit() and line[0].isdigit():
        raise ValueError("Invalid value. Symbol cannot start with integers.")
    
    # Process variable symbol
    else:
        # Check if the symbol is in the symbol table, if not push to symbol table
        if not parser.symbol_table.contains(line):
            parser.push_symbol(line)

        address = parser.symbol_table.retrive_address(line)
        return Code.compute_decimal_instruction(address)

def c_instruction(queue, parser):
    """
    Processes a C-instruction from the queue.

    Args:
        queue (str): A string representing the queue of C-instructions.
        parser(obj): parser object to call its methods

    Returns:
        str: The binary representation of the C-instruction.
    """
    line = queue

    #parsing the C-instruction into components
    comp_str = parser.comp(line)
    dest_str = parser.dest(line)
    jump_str = parser.jump(line)

    #translating to binary by calling methods from Code class object
    return "111" + Code.comp(comp_str) + Code.dest(dest_str)+ Code.jump(jump_str)

def write_to_file(queue, filepath, parser):
    """
    Writes the contents of the queue to a file specified by the filepath.

    Args:
        queue (Queue): A queue containing assembly instructions.
        filepath (str): The path to the file where the instructions will be written.
        parser(obj): parser object
    """
    with open(filepath, "w") as asm_file:
        while not queue.empty():    
            line = queue.get()
            # Check if the line is an A-instruction
            if line.startswith('@'):
                asm_file.write(a_instruction(line, parser) + '\n')               
            # C-instruction
            else:
                asm_file.write(c_instruction(line, parser) + '\n')

def run():
    """
    Runs the ASM.py Hack assembler.

    This function serves as the entry point for the Hack assembler.

    Note: The function assumes the existence of the Parser class and the write_to_file function.

    Raises:
        SystemExit: If there is an issue parsing command-line arguments.

    Example:
        To run the assembler:
        ```
        python ASM.py <input_filename>.asm
        ```
        This will process the input assembly code, generate the corresponding machine code,
        and save it to the output file with a '.hack' extension.
    """
    #command line processing
    arg_parser = argparse.ArgumentParser(description='Assemble Hack assembly code.')
    arg_parser.add_argument('input_filename', help='Input Hack assembly filename')
    args = arg_parser.parse_args()
    parser = Parser(args.input_filename)

    
    processed_asm = parser.ready_queue
    output_filename = args.input_filename.replace('.asm', '.hack')

    write_to_file(processed_asm, output_filename, parser)


run()