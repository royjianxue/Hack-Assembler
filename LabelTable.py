class LabelTable:
    
    def __init__(self):
        self.label_table = {}
   
    def contains(self, symbol):
        return symbol in self.label_table
      
    def add_entry(self, symbol, address):
        self.label_table[symbol] = address

    def retrive_address(self, symbol):
        try:
            return self.label_table[symbol]
        except KeyError:
            return None

