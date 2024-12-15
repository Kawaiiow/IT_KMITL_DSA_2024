"""CLASS??"""

class student:
    def __init__(self, name, gen, age, ids, gpa):
        self.name = name
        self.gen = gen
        self.age = age
        self.ids = ids
        self.gpa = gpa
        pass

    def query(self):
        print("Mr " if self.gen == "Male" else "Miss ", end="")
        print(f"{self.name} ({self.age}) ID: {self.ids} GPA {self.gpa:.2f}")

def main() -> None:
    """void"""
    list_std = []
    for _ in range (3):
        std = student(input(), input(), int(input()), input(), float(input()))
        list_std.append(std)
    target = input()
    res = None
    for obj in list_std:
        if obj.ids == target:
            res = obj
    if res == None:
        print("Student not found")
        return
    res.query()
main()
