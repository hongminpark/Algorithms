# Code referenced from https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/LinkedList.py


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(item)

    def print_(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def remove(self, item):
        if self.head.val is item:
            self.head = self.head.next
        else:

            # First, find item from the list
            cur = self.head
            while cur is not None:
                if cur.next.val is item:
                    cur.next = cur.next.next
                    break
                cur = cur.next

    # def remove(self, item):
    #     if self.head.val is item:
    #         self.head = self.head.next
    #     else:
    #
    #         # First, find item from the list
    #         cur = self.head
    #         while cur.next is not None:
    #             cur = cur.next
    #             if cur.val is item:
    #                 self.removeItem(item)
    #                 return
    #         print("Item doesn't exist in this Linked List")
    #
    # def removeItem(self, item):
    #     cur = self.head
    #     while cur is not None:
    #         if cur.next.val is item:
    #             cur.next = cur.next.next
    #             break
    #         cur = cur.next
    # # Remove and RemoveItem. Could I merge those two?

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        self.head = prev


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add(3)
    l_list.add(5)
    l_list.add(8)
    l_list.add(2)
    l_list.add(9)
    l_list.add(4)
    l_list.reverse()
    l_list.print_()
    l_list.remove(2)
    l_list.print_()
