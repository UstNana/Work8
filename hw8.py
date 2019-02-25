with open("HW8.txt") as f:
    while True:
        meal = f.readline().strip()
        ingredients = f.readline().strip()
        igr = f.readline().strip()
        print(meal, ingredients)
        if not meal:
            break
list_igr = igr.split()
print(list_igr)
