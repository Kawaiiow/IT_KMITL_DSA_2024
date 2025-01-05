
class DataNode:
    def __init__(self, name : str=""):
        self.data = name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def __init_first(self, data : any):
        self.head = DataNode(data)

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
            return
        cur_node : DataNode = self.head
        while cur_node:
            print(cur_node.data, end=' -> ' if cur_node.next else '\n')
            cur_node = cur_node.next
        

    def insert_last(self, data : any):
        if not self.head:
            self.__init_first(data)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = DataNode(data)
        self.count += 1

    def insert_front(self, data : any):
        if not self.head:
            self.__init_first(data)
        else:
            tmp = self.head
            self.head = DataNode(data)
            self.head.next = tmp
        self.count += 1       

    def insert_before(self, node : any, data : any):
        cur_node = self.head

        if not cur_node:
            print("Cannot insert,", node, "does not exist.")
            return
        if cur_node.data == node:
            self.insert_front(data)
            return
        while cur_node.next:
            if cur_node.next.data == node:
                break
            cur_node = cur_node.next
        if cur_node.next:
            tmp = cur_node.next
            cur_node.next = DataNode(data)
            cur_node.next.next = tmp
            self.count += 1
        else:
            print("Cannot insert,", node, "does not exist.")

    def delete(self, data):
        cur_node = self.head

        while cur_node:
            if cur_node.next.data == data:
                tmp = cur_node.next
                cur_node.next = cur_node.next.next
                del tmp
                return
            cur_node = cur_node.next
        if not cur_node:
            print("Cannot delete, does not exist.")

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #    mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()
main()
