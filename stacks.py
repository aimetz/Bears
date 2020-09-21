class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == len(self.items)

    def push(self, item):
        if not self.is_full():
            self.items[self.num_items] = item
            self.num_items += 1
        else:
            raise ValueError

    def pop(self):
        if self.num_items > 0:
            temp = self.items[self.num_items-1]
            self.items[self.num_items-1] = None
            self.num_items -= 1
            return temp
        else:
            raise ValueError

    def peek(self):
        return self.items[self.num_items-1]

    def size(self):
        return self.num_items
