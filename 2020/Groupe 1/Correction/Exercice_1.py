import random as rd

num = rd.randint(1,20)

for i in range(9, 0, -1):
    choice = int(input("Choisir un nombre: "))
    print(num)
    if choice > num:
        print(f"Il vous reste {i} vies, le nombre est plus petit.")
    elif choice < num:
        print(f"Il vous reste {i} vies, le nombre est plus grand.")
    elif choice == num:
        print(f"Vous avez gagné")
        break


