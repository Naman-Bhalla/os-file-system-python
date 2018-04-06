from src.file_system import FileSystem
from src.user import User

class OS:


    def __init__(self):
        self.open_files_table = {}
        self.process_files_table = {}
        self.users = set()
        self.system_user = User()
        self.users.add(self.system_user)
        self.root_file_system = FileSystem()

    def new_user(self):
        self.users.add(User())

    def open(self, file_name, mode):
        pass

    def close(self, file_name):
        pass
