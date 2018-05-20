# Source from https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/BinaryTree.py#L15

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(self.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(self.right, item)
                else:
                    return False

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    # remove action has 3 type
    # 1) no children
    # 2) 1 children
    # 3) 2 children
    def remove(self, item):
        if self.head.val is None:
            print("No ", item, "in BST")
        else:
            # When the head of the BST is the item
            if self.head.val == item:

                # 1) no children
                if self.head.left is None and self.head.right is None:
                    self.head = None

                # 2-1) 1 (right)children
                elif self.head.left is None and self.head.right is not None:
                    self.head = self.head.right

                # 2-2) 1 (left)children
                elif self.head.left is not None and self.head.right is None:
                    self.head = self.head.left

                # 3) 2 children : Change head value to the right most-left Node value
                #                 and remove the most_left node
                else:
                    self.head.val = self.most_left(self.head.right).val
                    self.remove_item(self.head, self.head.right, self.head.val)

            else:
                if item > self.head.val:
                    self._remove(self.head, self.head.right, item)
                else:
                    self._remove(self.head, self.head.left, item)

    # Getting the most left node from this BST
    def most_left(self, headNode):
        while True:
            if headNode.left is None:
                return headNode
            headNode = headNode.left

    # remove the link between parent and current
    def remove_item(self, parent, current, item):
        if current.val is item:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        else:
            if item > current.val:
                self.remove_item(current, current.right, item)
            else:
                self.remove_item(current, current.left, item)

    def _remove(self, parent, current, item):
        if current is None:
            print("No ", item, "in BST")
        else:
            if current.val is item:
                if current.left is None and current.right is None:
                    if parent.left is current:
                        parent.left = None
                    else:
                        parent.right = None

                elif current.left is None and current.right is not None:
                    if parent.left is current:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                elif current.left is not None and current.right is None:
                    if parent.left is current:
                        parent.left = current.left
                    else:
                        parent.right = current.left

                else:
                    current.val = self.most_left(current.right).val
                    self.remove_item(current, current.right, item)

    def preorder_traverse(self):
        # 1) Visit the root
        # 2) Traverse the left subtree
        # 3) Traverser the right subtree
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print(cur.val)

        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        print(cur.val)

