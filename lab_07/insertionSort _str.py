import json

def insertionSort(arr : list, last : int) -> None:
    cmp = 0
    for i in range(1, last + 1):
        key = arr[i]
        j = i - 1
        while True:
            if j >= 0:
                cmp += 1
            if j >= 0 and key[0] < arr[j][0]:
                arr[j + 1] = arr[j]
                j -= 1
            elif j >= 0 and key[0] == arr[j][0] and int(key[1:]) < int(arr[j][1:]):
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
        print(arr)
    print(f"Comparison times: {cmp}")

def main() -> None:
    arr = json.loads(input())
    insertionSort(arr, int(input()))
main()