import random as rd

choices = [1, 2, 3]
#[ordi, joueur, message]
winning = [(2,1, "L'ordinateur a gagné"),
            (3,2, "L'ordinateur a gagné"),
            (1,3, "L'ordinateur a gagné"),
            (1,2, "Vous avez gagné"),
            (2,3, "Vous avez gagné"),
            (3,1, "Vous avez gagné")]

for i in range(3):
    computer_choice = rd.choice(choices)
    choice = int(input("Faites votre choix: 1)Pierre, 2)Feuille, 3)Ciseaux: "))  
    for j in winning:
        if (computer_choice, choice) == j[:2]:
            print(j[2])