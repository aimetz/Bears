class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def push(self, item):
        if not self.is_full():
            self.items[self.num_items] = item
            self.num_items += 1
        else:
            raise IndexError

    def pop(self):
        if not self.is_empty():
            self.num_items -= 1
            return self.items[self.num_items]
        raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.items[self.num_items - 1]
        raise IndexError

    def size(self):
        return self.num_items
