my_file = open("quarterbacks.txt", "a")

print("What qb do you want to add?\n")
newqb = input()

my_file.writelines("\n" + newqb)

my_file.close()

