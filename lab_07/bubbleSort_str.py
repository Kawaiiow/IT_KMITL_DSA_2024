import json

def bubbleSort(arr : list, last : int) -> None:
    i       : int = 0
    j       : int = last
    cmp     : int = 0
    stat    : bool = False

    while i <= last and not stat:
        j = last
        stat = True
        while j > i:
            cmp += 1
            if arr[j][0] < arr[j - 1][0]:
                stat = False
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            elif arr[j][0] == arr[j - 1][0] and int(arr[j][1:]) < int(arr[j - 1][1:]):
                stat = False
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        print(arr)
        i += 1
    print(f"Comparison times: {cmp}")
    return

def main() -> None:
    bubbleSort(json.loads(input()), int(input()))
main()
