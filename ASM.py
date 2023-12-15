from Parser import Parser
    
parser = Parser('Max.asm')


if __name__ == "__main__":

    parser.print_queue_contents(parser.firstpass)