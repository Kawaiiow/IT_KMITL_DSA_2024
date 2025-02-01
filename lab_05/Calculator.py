
def main():
    n = int(input())
    presses = 1
    for i in range(1, n + 1):
        presses += len(str(i))
        if i < n:
            presses += 1
    print(presses)
main()
