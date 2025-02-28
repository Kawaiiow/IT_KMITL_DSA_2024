import json

def selectionSort(arr : list, last : int) -> None:
    i = 0
    cmp = 0
    while i < last:
        k = i
        j = i + 1
        while j <= last:
            cmp += 1
            if arr[j][0] < arr[k][0]:
                k = j
            elif arr[j][0] == arr[k][0] and int(arr[j][1:]) < int(arr[k][1:]):
                k = j
            j += 1
        arr[i], arr[k] = arr[k], arr[i]
        print(arr)
        i += 1
    print(f"Comparison times: {cmp}")
    return

def main() -> None:
    selectionSort(json.loads(input()), int(input()))
main()
