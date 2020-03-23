class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def adding(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def del_head(self):
        current = self.head.data
        self.head = self.head.next
        return current

    def del_end(self):
        list = []
        current = self.head
        list.append(current.data)
        while current.next:
            current = current.next
            list.append(current.data)
        del list[-1]
        print(list)

    def length(self):
        current = self.head
        total = 1
        while current.next:
            total += 1
            current = current.next
        print(total)

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        return elems

    def show_any(self, index):
        list = []
        current = self.head
        list.append(current)
        while current.next:
            current = current.next
            list.append(current)
        if index > len(list):
            print("ERROR. Out of range")
        print(list[index])

    def erase_by_index(self, index):
        list = []
        current = self.head
        list.append(current)
        while current.next:
            current = current.next
            list.append(current)
        if index > len(list):
            print("ERROR. Out of range")
        del list[index]
        print(list)

    def rem_obj(self, object):
        list = []
        current = self.head
        list.append(current.data)
        if int(object) in list: list.remove(object)
        while current.next:
            current = current.next
            list.append(current.data)
        if int(object) in list: list.remove(object)
        elif int(object) not in list: print("Error. No such value")
        print(list)

    def contains_or_not(self, object):
        list = []
        current = self.head
        list.append(current.data)
        while current.next:
            current = current.next
            list.append(current.data)
        if int(object) in list: print(True)
        else: print(False)

    def clear(self):
        current = self.head
        current.data = None
        while current.next:
            current = current.next
            current.data = None