import SymbolTable
import Parser

class ASM:
    
    def __init__(self):
        pass


    def assemble(code):
        pass


if __name__ == "__main__":
    # Example usage
    code = """
    // This is a sample code
    @21
    M=1
    @i
    M=M+1;JMP
    """
    binary_code = assemble(code.split('\n'))
    print(binary_code)
