class File:
    name = ""
    content = ""
    def __init__(self, name, content = ""):
        self.name = name
        self.content = content

class Dir:
    name = ""
    files = []
    dirs = []
    def __init__(self, name="", dirs = [], files = []):
        self.name = name
        self.dirs = dirs
        self.files = files

    def add_file(self, file):
        self.files.append(file)
        return self

    def add_dir(self, dir):
        self.dirs.append(dir)
        return self

    def for_each_dir(self, func):
        for dir in self.dirs:
            func(dir)

    def for_each_file(self, func):
        for file in self.files:
            func(file)

class PC:
    root = None
    def __init__(self, root = Dir("root")):
        self.root = root



def random_root():
    file1 = File("file1", "file1 content")
    file2 = File("file2", "file2 content")
    dir1 = Dir("dir1")
    dir1.add_file(file1).add_file(file2)
    root = Dir("root", [dir1])
    return root

def random_pc():
    return PC(random_root())

if __name__ == "__main__":
    root = random_root()
    root.for_each_dir(lambda x : print(f"dir : {x}"))