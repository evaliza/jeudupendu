import random

choose = ["python", "developpeur", "clavier", "souris", "internet"]
solution = random.choice(choose) # choisirt au hasard un mot

# key_solution = random.uniform(0, len(choose)-1) # prendre la clé du mot, pas ok, chiffre float
# print(key_solution)
#print(random.randrange(10)) # chiffre de 0 à 9 en int
key_solution = random.randrange(len(choose))
solution = choose[key_solution]

#initialisation des variables
attempts = 0
display = ""
letter_found = ""

for l in solution:
    #mettre autant de "_" que de lettre
    display = display + "_ "

print(">> Bienvenue dans le pendu <<")

while attempts < 7:
    print("\nMot à deviner : ", display)
    proposition = input("proposez une lettre : ")[0:1].lower() # je prends uniquement la première lettre [0:1] et là met en miniscule

    if proposition in solution:
        # je verifie si la lettre se trouve dans le mot
        letter_found = letter_found + proposition
        print("-> Bien vu!")
    else:
        print("-> Dommage\n")
        if attempts == 6:
            print(" ==========Y= ")
        if attempts >= 5:
            print(" ||/       |  ")
        if attempts >= 4:
            print(" ||        0  ")
        if attempts >= 3:
            print(" ||       /|\ ")
        if attempts >= 2:
            print(" ||       /|  ")
        if attempts >= 1:
            print("/||           ")
        if attempts >= 0:
            print("==============\n")

        attempts += 1

    #je construis le mot à afficher avec les _ si les lettres ne sont pas trouvées
    display = ""
    for x in solution:
        #je parcour le lettre du mot à trouver
        if x in letter_found:
            #je verifie se trouve dans letter-found
            # si ok l ajouter ds la variable display sion mettre "_"
            display += x + " "
        else:
            display += "_ "

    if "_" not in display:
        #il y a plus de "_" toute les lettres trouvées
        print("c est Gagné!")
        break

print("\n    * Fin de la partie *    ")