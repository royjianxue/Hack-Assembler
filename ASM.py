from Parser import Parser
from Code import Code

def a_instruction(queue):
    line = queue[1::]
    if line.isdigit():
        return Code.compute_decimal_instruction(line)
    elif not line.isdigit() and line[0].isdigit():
        raise ValueError("Invalid value. Symbol cannot start with integers.")
    else:
        if not parser.symbol_table.contains(line):
            parser.push_symbol(line)
        address = parser.symbol_table.retrive_address(line)
        return Code.compute_decimal_instruction(address)

def c_instruction(queue):
    line = queue
    comp_str = parser.comp(line)
    dest_str = parser.dest(line)
    jump_str = parser.jump(line)
    return "111" + Code.comp(comp_str) + Code.dest(dest_str)+ Code.jump(jump_str)

def write_to_file(queue, filepath):
    with open(filepath, "w") as asm_file:
        while not queue.empty():
            line = queue.get()
            if line.startswith('@'):
                asm_file.write(a_instruction(line) + '\n')
            else:
                asm_file.write(c_instruction(line) + '\n')

parser = Parser('Max.asm')

processed_asm = parser.ready_queue

write_to_file(processed_asm, 'newfile.asm')

