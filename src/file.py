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
        self.current_pointer = 0
        self.data = []


    def write(self, data):
        pass

    def read(self, index):
        pass

    def reposition_index(self, value):
        pass

    def delete(self):
        pass

    def truncate(self, length):
        pass

    def __str__(self):
        pass

    def is_directory(self):
        return False