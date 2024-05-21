import csv

def charger_pokemon_csv(csv_file):
    dictionnary = {}
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        compteur = 0
        for row in csv_reader:
            if compteur == 0:
                pass
                compteur += 1
            else:
                dictionnary[row[0]] = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])]
                compteur += 1
    return dictionnary

pkmn = charger_pokemon_csv("pokemon.csv")

for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
