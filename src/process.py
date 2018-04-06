class Process:


    def __init__(self, directory):
        self.current_file = None
        self.current_directory = directory

    def open_file(self):
        pass

    def read_next(self):
        pass

    def write_next(self, data):
        pass

    def reset_file_pointer(self):
        pass

    def read(self, index):
        pass

    def write(self, index):
        pass

    def skip(self, index):
        pass