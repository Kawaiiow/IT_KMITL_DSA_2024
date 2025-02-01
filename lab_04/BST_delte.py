
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
        if not self.root or not self.root.data:
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

    def delete(self, data : int):
        cur = self.root
        self.root = self._remove(cur, data)

    def _remove(self, root : BSTNode, data : int):
        if root is None:
            print("Delete Error,", data, "is not found in Binary Search Tree.")
            return root
        
        if data < root.data:
            root.left = self._remove(root.left, data)
            return root
        elif data > root.data:
            root.right = self._remove(root.right, data)
            return root

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        target_par = root
        target = root.left
        while target.right is not None:
            target_par = target
            target = target.right

        root.data = target.data

        if target_par.right == target:
            target_par.right = target.left
        else:
            target_par.left = target.left
        return root

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()
