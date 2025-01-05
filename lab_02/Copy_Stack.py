# from Array_stack import ArrayStack

class ArrayStack:
    def __init__(self) -> None:
        self.size : int = 0
        self.data : list = list()
        pass

    def push(self, content) -> None:
        try:
            if content.isdigit():
                content = int(content)
            elif content.replace(".", "", 1).isdigit():
                content = float(content)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(content)
            self.size += 1

    def pop(self) -> str | int | float:
        if self.size:
            self.size -= 1
            return (self.data.pop())
        else:
            print("Underflow: Cannot pop data from an empty list")
            return (None)
        
    def is_empty(self) -> bool:
        if not self.size:
            return True
        return False
    
    def get_stack_top(self) -> str | int | float:
        if self.size:
            con = self.pop()
            self.push(con)
            return (con)
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return (None)

    def get_size(self) -> int:
        return (self.size)
    
    def print_stack(self):
        print(self.data)

def copy_stack(stack1: ArrayStack, stack2: ArrayStack):
    """void"""
    tmp_stack : ArrayStack = ArrayStack()
    tmp = 0

    while stack2.size:
        stack2.pop()
    while stack1.size:
        tmp_stack.push(stack1.pop())
    while tmp_stack.size:
        tmp = tmp_stack.pop()
        stack1.push(tmp)
        stack2.push(tmp)

def print_status():
  """Print all stacks"""
  print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
  STACK1_.print_stack()
  print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
  STACK2_.print_stack()
  print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
  STACK3_.print_stack()
  print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
  STACK4_.print_stack()
  print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()

STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
  STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
  STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
  TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))

