from uuid import uuid4
from src.directory import Directory
from src.process import Process

class User:
    def __init__(self):
        self.unique_id = uuid4()
        self.processes = []
        self.current_directory = str(self.unique_id)
        self.root_directory = Directory(self.current_directory)

    def createProcess(self):
        self.processes.append(Process(self.current_directory))