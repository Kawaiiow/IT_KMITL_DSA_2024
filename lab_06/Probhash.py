class Student:
    def __init__(self, std_id : int, name : str, gpa : float):
        self.std_id = int(std_id)
        self.name = name
        self.gpa = float(gpa)

    def get_std_id(self) -> int:
        return self.std_id
        
    def get_name(self) -> str:
        return self.name
        
    def get_gpa(self) -> float:
        return self.gpa
        
    def print_details(self) -> None:
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, size : int):
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key : int) -> int:
        return key % self.size

    def rehash(self, key : int) -> int:
        return (key + 1) % self.size


    def insert_data(self, std : Student) -> None:
        lp = 0
        pos = self.hash(std.get_std_id())
        while self.hash_table[pos] != None and lp < self.size:
            lp += 1
            pos = self.rehash(pos)
        if lp >= self.size:
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        print(f"Insert {std.std_id} at index {pos}")
        self.hash_table[pos] = std

    def search_data(self, std_id : int) -> Student:
        lp = 0
        pos = self.hash(std_id)

        if self.hash_table[pos] == None:
            print(f"{std_id} does not exist.")
            return None
        
        while self.hash_table[pos] != None and self.hash_table[pos].std_id != std_id and lp < self.size:
            lp += 1
            pos = self.rehash(pos)

        if self.hash_table[pos] == None  or lp >= self.size:
            print(f"{std_id} does not exist.")
            return None
        
        print(f"Found {std_id} at index {pos}")
        return self.hash_table[pos]

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
