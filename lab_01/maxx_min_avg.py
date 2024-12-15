""" MMA """

import json

def main() -> None :
    """void"""
    n_arr = json.loads(input())
    low = n_arr[0]
    high = n_arr[0]
    total = 0
    
    for n in n_arr:
        if n < low:
            low = n
        if n > high:
            high = n
        total += n
    print(f"({high}, {low}, {(total / len(n_arr)):.2f})")
main()
