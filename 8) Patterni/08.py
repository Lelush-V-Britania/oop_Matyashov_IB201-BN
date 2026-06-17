class FileSystemElement:
    def display(self, indent=""):
        pass

    def get_size(self):
        pass

class File(FileSystemElement):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=""):
        print(f"{indent}📄 {self.name} ({self.size} bytes)")

    def get_size(self):
        return self.size

class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, element):
        self.children.append(element)

    def display(self, indent=""):
        print(f"{indent} {self.name}/")
        for child in self.children:
            child.display(indent + "  ")

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total