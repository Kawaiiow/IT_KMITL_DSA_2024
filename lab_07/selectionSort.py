import json

def selectionSort(arr : list, last : int) -> None:
    i = 0
    cmp = 0
    while i < last:
        k = i
        j = i + 1
        while j <= last:
            cmp += 1
            if arr[j] < arr[k]:
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
