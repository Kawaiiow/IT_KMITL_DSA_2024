import json

class Student:
    def __init__(self, std_id : int, name : str, gpa : float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self) -> int:
        return self.std_id
        
    def get_name(self) -> str:
        return self.name
        
    def get_gpa(self) -> float:
        return self.gpa
        
    def print_details(self) -> None:
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

def binary_search(arr_std : list, target : str) -> None:
    cmp_count = 0
    start = 0
    end = len(arr_std) - 1
    while start <= end:
        cmp_count += 1
        mid = (start + end) // 2
        if target > arr_std[mid].name:
            start = mid + 1
        elif target < arr_std[mid].name:
            end = mid - 1
        else:
            start = end + 1
    if (target == arr_std[mid].name):
        print(f"Found {target} at index {mid}")
        arr_std[mid].print_details()
    else:
        print(f"{target} does not exists.")
    print(f"Comparisons times: {cmp_count}")
    return

def main() -> None:
    buc : list = json.loads(input())
    arr_std = []
    for o in buc:
        arr_std.append(Student(o["id"], o["name"], o["gpa"]))
    binary_search(arr_std, input())
main()
