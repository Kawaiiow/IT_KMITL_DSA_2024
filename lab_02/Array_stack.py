
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
        
    def is_empty(self) -> bool:
        if not self.size:
            return True
        return False
    
    def get_stack_top(self) -> str | int | float:
        if self.size:
            return (self.data[self.size - 1])
        else:
            print("Underflow: Cannot pop data from an empty list")

    def get_size(self) -> int:
        return (self.size)
    
    def print_stack(self):
        print(self.data)

# def main():
#     s1 = ArrayStack()
#     s2 = ArrayStack()
#     s1.push(10)
#     s1.push(20)
#     s1.push(30)
#     s2.push(25)
#     x = s1.pop()
#     s2.push(x)
#     s1.print_stack()
#     s2.print_stack()
# main()
