
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

def main():
    stack = ArrayStack()
    text_in = input()
    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
        text_in = input()
    stack.print_stack()

main()

