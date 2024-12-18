from Array_stack import ArrayStack

def is_parentheses_matching(expression) -> bool:
    """boolean"""
    s1 = ArrayStack()
    s2 = ArrayStack()
    close_brack = 0
    stat = True

    for c in expression:
        s1.push(c)
    if s1.get_stack_top() == ')':
        close_brack += 1
    s2.push(s1.pop())
    while stat and s1.size:
        if s1.get_stack_top() in ('+', '-', '*', '/', '%') and \
            (s2.get_stack_top not in ('+', '-', '*', '/', '%')):
            s2.push(s1.pop())
        elif s1.get_stack_top() == ')' and \
            s2.get_stack_top() in ('+', '-', '*', '/', '%', ')'):
            s2.push(s1.pop())
            close_brack += 1
        elif s1.get_stack_top() == '(' and \
            s2.get_stack_top() not in ('+', '-', '*', '/', '%', ')') and \
            close_brack:
            s2.push(s1.pop())
            close_brack -= 1
        elif str(s1.get_stack_top()).isalnum and \
            not s2.get_stack_top().isalnum() and \
                s2.get_stack_top() != '(':
            s2.push(s1.pop())
        else:
            stat = False
    if close_brack:
        stat = False
    if not stat:
        print("Parentheses in", expression, "are unmatched​")
    return stat

def main() -> None:
    """void"""
    exprs = input()
    is_parentheses_matching(exprs)
main()
