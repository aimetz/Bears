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
    if self.num_items == 0:
        self.items[0] = item
        self.num_items += 1
    elif self.num_items < self.capacity:
        for i in range(self.num_items):
            self.items[self.num_items - i] = self.items[self.num_items - (i + 1)]
        self.items[0] = item
        self.num_items += 1
    else:
        raise ValueError


def pop(self):
    if self.num_items > 0:
        temp = self.items[0]
        for i in range(self.num_items):
            self.items[i] = self.items[i + 1]
        self.items[self.num_items - 1] = None
        self.num_items -= 1
        return temp
    else:
        raise ValueError


def peek(self):
    return self.items[0]


def size(self):
    return self.num_items


a = StackArray(10)
print(is_empty(a))
push(a, "Hi")
push(a, "this")
push(a, "is")
push(a, "a")
pop(a)
print(peek(a))
push(a, "Stack")
print(peek(a))
print(size(a))
