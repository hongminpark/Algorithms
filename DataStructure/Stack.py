class Stack:

    def __init__(self):
        self.itemList = []
        self.maxSize = 100

    def push(self, item):
        if self.size is self.maxSize:
            print("Stack Overflow")
        else:
            self.itemList.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            return self.itemList.pop()

    def print_(self):
        print(self.itemList)

    def size(self):
        return len(self.itemList)

    def is_empty(self):
        if self.size is 0:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(1)
    stack.push(5)
    stack.pop()
    stack.pop()
    stack.print_()
