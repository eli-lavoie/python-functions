def poultry_primate():
    for x in range(1, 101):
        if x % 7 == 0 and x % 5 == 0:
            print("ChickenMonkey")
        elif x % 5 == 0:
            print("Chicken")
        elif x % 7 == 0:
            print("Monkey")
        else:
            print(x)

poultry_primate()