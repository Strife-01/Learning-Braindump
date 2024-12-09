fname = input("Fname: ")

total_grades = 0
wanted_grades = 0


with open(fname) as fhand:
    for line in fhand:
        words = line.strip().split()
        num = words[-1]
        try:
            if float(num.replace(",", ".")) >= 9.8:
                wanted_grades += 1
            total_grades += 1
        except:
            continue


print(f"total: {total_grades}, >9.8: {wanted_grades}")
print(f"{wanted_grades * 100 / total_grades:.2f}%")
