from uuid import uuid4
from datetime import date
from file import File

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
        for files in self.sub_files:
            if files.name == file_name:
                return files

    def create(self, file_name):
        self.sub_files.append(File(file_name, '')) # TODO

    def delete(self, force):
        if not self.isEmpty() and not force:
            return False
        del self.sub_files
        return True

    def rename(self, initial_name, final_name):
        for files in self.sub_files:
            if files.name == initial_name:
                files.name = final_name
                return True
        return False

    def traverse(self):
        for anything in self.sub_files:
            print(anything.name)

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

    def isEmpty(self):
        if self.sub_files:
            return False
        return True
