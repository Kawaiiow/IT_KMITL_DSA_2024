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

def main() -> None:
    """void"""
    m = int(input())
    n = int(input())
    pool = ArrayStack()
    group = list()

    for i in range (m):
        group.append(ArrayStack());
    for _ in range (n):
        pool.push(input())
    while not pool.is_empty():
        for g in group:
            if not pool.is_empty():
                tmp = pool.pop()
                g.push(tmp)
    idx = 1
    for g in group:
        buf = f"Group {idx}: "
        buf += str(g.data).replace("[","").replace("]","").replace("'","")
        print(buf)
        idx += 1
main()
