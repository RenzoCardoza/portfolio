import csv

class DictionaryReader():

    def __init__(self, filename):
        """initializes the main values"""

        #attributes
        self.file = filename
        self.reader = csv.reader(self.file)
    
    def read_file(self):
        """read the file and convert it to dictionary"""
        
        #skips the next line
        self.reader(next)

    def create_file(self):
        """cretes the file if there is no file"""

        
