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

def is_parentheses_matching(expression) -> bool:
    """boolean"""
    stack = ArrayStack()
    stat = True

    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            con = stack.pop()
            if not con:
                stat = False
    if not stack.is_empty():
        stat = False
    return stat

def main() -> None:
    """void"""
    exprs = input()
    b = is_parentheses_matching(exprs)
    if b:
        print(f"Parentheses in {exprs} are matched")
    else:
        print(f"Parentheses in {exprs} are unmatched")
    print(b)
main()
