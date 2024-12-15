"""OOP?"""

def main() -> None :
    """void"""
    name = []
    gen = []
    age = []
    ids = []
    gpa = []
    for i in range (3):
        name.append(input())
        gen.append(input())
        age.append(int(input()))
        ids.append(input())
        gpa.append(float(input()))
    target = input()
    if not target in ids:
        print("Student not found")
        return
    idx = ids.index(target)
    res = ""
    res += "Mr " if gen[idx] == "Male" else "Miss "
    res += name[idx] + " "
    res += "("
    res += str(age[idx])
    res += ") "
    res += "ID: "
    res += str(ids[idx])
    res += " "
    res += "GPA "
    res += "%.2f" % gpa[idx]
    print(res)
    # print(gpa[idx]:.2f)
main()
