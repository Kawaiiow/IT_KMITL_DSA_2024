
import json

def main():
    a = json.loads(input())
    b = json.loads(input())
    c = json.loads(input())

    for n in a:
        if n in b and n in c:
            print(True)
            return
    print(False)
main()
