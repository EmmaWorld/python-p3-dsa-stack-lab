class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item) if len(self.items) < self.limit else 'Stack is at limit'

    def pop(self):
        return None if len(self.items) == 0 else self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

    def full(self):
         return len(self.items) == self.limit

    def search(self, target):
        distance = 0
        for item in reversed(self.items):
            if item == target:
                return distance
            distance += 1
        return -1