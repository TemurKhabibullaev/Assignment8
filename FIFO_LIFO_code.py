from LinkedList import SinglyLinkedList


class UniversalMethod:
    def __init__(self):
        self.ins = SinglyLinkedList()

    def add_head(self, data):
        self.ins.add_head(data)

    def del_head(self):
        return self.ins.del_head()

    def add_end(self, data):
        self.ins.adding(data)

    def display(self):
        return self.ins.display()
