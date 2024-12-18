from Array_stack import ArrayStack

def copyStack(stack1: ArrayStack, stack2: ArrayStack):
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

def main() -> None:
    """void"""
    s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
    s2 = ArrayStack(); s2.push(15)
    copyStack(s1, s2)
    s1.print_stack()
    s2.print_stack()
main()
