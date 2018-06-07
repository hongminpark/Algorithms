class Queue:
    def __init__(self):
        self.itemList = []

    def en_queue(self, item):
        self.itemList.append(item)

    def de_queue(self):
        if self.is_empty():
            print("No item in this queue")
        else:
            return self.itemList.pop(0)

    def print_(self):
        print(self.itemList)

    def is_empty(self):
        if self.size() is 0:
            return True
        else:
            return False

    def size(self):
        return len(self.itemList)


if __name__ == "__main__":
    queue = Queue()
    queue.en_queue(2)
    queue.en_queue(1)
    queue.en_queue(4)
    queue.en_queue(5)
    queue.en_queue(7)
    queue.de_queue()
    queue.de_queue()
    queue.print_()

