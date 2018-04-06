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
            self.last_modified = date.today()

    def read(self, index):
        return self.data[index]

    def reposition_index(self, value):
        if value <= self.size:
            return True
        return False

    def delete(self):
        del self.data

    def truncate(self, length):
        self.size = length
        self.data = self.data[ : self.size]

    def __str__(self):
        pass

    def is_directory(self):
        return False
