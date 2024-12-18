from Array_stack import ArrayStack

def main() -> None:
    """void"""
    stack = ArrayStack()
    g1 = ArrayStack()
    g2 = ArrayStack()

    stdin = input()
    while stdin:
        stack.push(stdin)
        stdin = input()
    while stack.size:
        if stack.size:
            g1.push(stack.pop())
        if stack.size:
            g2.push(stack.pop())
    g1.print_stack()
    g2.print_stack()
main()
