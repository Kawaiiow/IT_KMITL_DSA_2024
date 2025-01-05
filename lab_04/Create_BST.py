
class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

def main():
    tree = BSTNode(int(input()))
    print(tree.data)
    print(tree.left)
    print(tree.right)
main()
