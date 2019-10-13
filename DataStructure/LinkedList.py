class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)
        else:
            self.head = Node(item)

    def remove(self, item):
        if self.head.value == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next:
                if cur.next.value == item:
                    cur.next = cur.next.next
                    break
                cur = cur.next

    def reverse(self):
        before = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = before
            before = cur
            cur = next
        self.head = before

    def print(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        print(result)


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.add(3)
    linkedlist.add(5)
    linkedlist.add(2)
    linkedlist.add(7)
    linkedlist.add(5)
    linkedlist.add(7)
    linkedlist.add(9)
    linkedlist.reverse()
    linkedlist.print()
    linkedlist.remove(7)
    linkedlist.print()

