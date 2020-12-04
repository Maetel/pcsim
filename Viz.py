import PC
import PyQt5.QtWidgets


class Viz:
    def __init__(self):
        pass

    def print(self, pc):
        root = pc.root
        root.for_each_dir(lambda x:print(x.name))
        root.dirs[0].for_each_file(lambda x:print(f"name = {x.name} content = {x.content}"))

if __name__ == "__main__":
    PC = PC.random_pc()
    viz = Viz()
    viz.print(PC)
