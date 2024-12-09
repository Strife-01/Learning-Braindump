l = [100, 10, 15, 25, 70]
wanted = int(input("Number: "))

for num in l:
    if num == wanted:
        print(f"{wanted} is in the list")
        break
else:
    print(f"{wanted} is not in the list")