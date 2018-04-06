from uuid import uuid4
from datetime import date


class File:

    def __init__(self, name, parent_location):
        self.id = uuid4()
        self.name = name
        self.location = parent_location + '/' + name
        self.size = 0
        self.date_created = date.today()
        self.last_modified = self.date_created
        self.data = []


    def write(self, index, data):
        self.data[index] = data
        if index > self.size:
            self.size = index

    def read(self, index):
        return self.data[index]

    def reposition_index(self, value):
        if value < self.size:
            return False
        return True

    def delete(self):
        pass

    def truncate(self, length):
        pass

    def __str__(self):
        pass

    def is_directory(self):
        return False