class Process:


    def __init__(self, directory):
        self.current_file = None
        self.current_directory = directory
        self.current_index = None

    def open_file(self):
        pass

    def read_next(self):
        if self.current_file:
            file = self.current_file
            if (self.current_index + 1) < self.current_file.size:
                return file.read(self.current_index + 1)

    def write_next(self, data):
        if self.current_file:
            if (self.current_index + 1) < self.current_file.size:
                file = self.current_file
                for i in range(len(data)):
                    file.write(self.current_index + 1 + i, data[i])
                return True

        return False

    def reset_file_pointer(self):
        self.current_index = 0

    def read(self, index):
        if self.current_file:
            if index < self.current_file.size:
                file = self.current_file
                return file.read(index)

    def write(self, index, data):
        if self.current_file:
            if index < self.current_file.size:
                file = self.current_file
                for i in range(len(data)):
                    file.write(index + i, data[i])
                return True

        return False


    def skip(self, index):
        if self.current_file:
            file = self.current_file
            if file.reposition_index(self.current_index + index):
                self.current_index += index
                return True

        return False
