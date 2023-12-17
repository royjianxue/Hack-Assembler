class Code:
    """
    Class containing static methods for handling Hack assembly code translations.
    """

    # Dictionary mapping computation mnemonics to binary codes
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

    # Dictionary mapping destination mnemonics to binary codes
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

    # Dictionary mapping jump mnemonics to binary codes
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
        """
        Translates the computation mnemonic to its binary code.

        Args:
            comp_str (str): The computation mnemonic.

        Returns:
            str: The binary code corresponding to the computation mnemonic.

        Raises:
            KeyError: If the computation mnemonic is not found.
        """
        try:
            return Code.comp_codes[comp_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your comp key!")
        
    @staticmethod    
    def dest(dest_str):
        """
        Translates the destination mnemonic to its binary code.

        Args:
            dest_str (str): The destination mnemonic.

        Returns:
            str: The binary code corresponding to the destination mnemonic.

        Raises:
            KeyError: If the destination mnemonic is not found.
        """
        try:
            if dest_str == '':
                dest_str = 'null'
                return Code.dest_codes[dest_str]
            return Code.dest_codes[dest_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your dest key!")
        
    @staticmethod
    def jump(jump_str):
        """
        Translates the jump mnemonic to its binary code.

        Args:
            jump_str (str): The jump mnemonic.

        Returns:
            str: The binary code corresponding to the jump mnemonic.

        Raises:
            KeyError: If the jump mnemonic is not found.
        """
        try:
            if jump_str == '':
                jump_str = 'null'    
                return Code.jump_codes[jump_str]
            return Code.jump_codes[jump_str]
        except KeyError:
            raise KeyError("Invalid Symbol, check your jump key")
    
    @staticmethod
    def compute_decimal_instruction(decimal_value_str):
        """
        Converts a decimal value string to its 16-bit binary representation.

        Args:
            decimal_value_str (str): The decimal value string.

        Returns:
            str: The 16-bit binary representation of the decimal value.

        Raises:
            ValueError: If the decimal value string is not a valid integer.
        """
        try:
            decimal_value = int(decimal_value_str)
        except ValueError:
            raise ValueError("Invalid decimal value: {}".format(decimal_value_str))
        binary_string = format(decimal_value, '016b')
        return binary_string
    