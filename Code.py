from LabelTable import LabelTable

class Code:

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

    @staticmethod
    def comp(comp_str):
        try:
            return Code.comp_codes[comp_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your comp key!")
    @staticmethod    
    def dest(dest_str):
        try:
            return Code.dest_codes[dest_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your dest key!")
    @staticmethod
    def jump(jump_str):
        try:
            if jump_str == '':
                jump_str = 'null'    
                return Code.jump_codes[jump_str]
            return Code.jump_codes[jump_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your jump key")
    @staticmethod
    # labeltable is an instance of LabelTable class
    def label(label_str, labeltable):
        return labeltable.label_table[label_str]
    
    @staticmethod
    def compute_decimal_instruction(decimal_value_str):
        try:
            decimal_value = int(decimal_value_str)
        except ValueError:
            raise ValueError("Invalid decimal value: {}".format(decimal_value_str))
        
        binary_string = format(decimal_value, '016b')
        return binary_string
    
if __name__ == "__main__":

    print(Code.compute_decimal_instruction("21"))
    print("111" + Code.comp('D+1') + Code.dest('MD')+ Code.jump(''))