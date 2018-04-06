from uuid import uuid4
from datetime import date

class Directory:

    def __init__(self, name):
        self.id = uuid4()
        self.name = name
        self.size = 0
        self.date_created = date.today()
        self.last_modified = self.date_created
        self.sub_files = []

    def is_directory(self):
        return True

    def search(self, file_name):
        pass

    def create(self, file_name):
        pass

    def delete(self):
        pass

    def rename(self, initial_name, final_name):
        pass

    def traverse(self):
        pass

    def delete_file(self, file_name):
        i = -1
        for files in self.sub_files:
            i += 1
            if not files.is_directory() and files.name == file_name:
                self.size -= files.size
                self.last_modified = date.today()
                self.sub_files.pop(i)
                files.delete()
                return True
        return False
