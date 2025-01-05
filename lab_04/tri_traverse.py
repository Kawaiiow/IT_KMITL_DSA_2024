
class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root : BSTNode = BSTNode()

    def insert(self, data : int):
        cur = self.root

        if data == None:
            return
        if not self.root.data:
           self.root.data = data
           return
        while 1:
            while cur.left and data <= cur.data:
                cur = cur.left
            while cur.right and data > cur.data:
                cur = cur.right
            if not cur.right and data > cur.data:
                cur.right = BSTNode(data)
                return
            elif not cur.left and data <= cur.data:
                cur.left = BSTNode(data)
                return

    def is_empty(self):
        return (True if not self.root.data else False)

    def preorder(self):
        print("Preorder:", end="")
        def pre_recur(cur):
            print(" -> ", end="")
            print(cur.data, end="")
            if cur.left:
                pre_recur(cur.left)
            if cur.right:
                pre_recur(cur.right)
        pre_recur(self.root)
        print()

    def inorder(self):
        print("Inorder:", end="")
        def in_order(cur):
            if cur.left:
                in_order(cur.left)
            print(" -> ", end="")
            print(cur.data, end="")
            if cur.right:
                in_order(cur.right)
        in_order(self.root)
        print()

    def postorder(self):
        print("Postorder:", end="")
        def post_order(cur):
            if cur.left:
                post_order(cur.left)
            if cur.right:
                post_order(cur.right)
            print(" -> ", end="")
            print(cur.data, end="")
        post_order(self.root)
        print()

    def traverse(self):
        if not self.root.data:
            print("This is an empty binary search tree.")
            return
        self.preorder()
        self.inorder()
        self.postorder()

    def find_min(self):
        cur = self.root

        while cur.left:
            cur = cur.left
        return (cur.data)

    def find_max(self):
        cur = self.root

        while cur.right:
            cur = cur.right
        return (cur.data)

    # def delete(self, data : int):


def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()

main()
