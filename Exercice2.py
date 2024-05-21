import csv

def charger_pokemon_csv(csv_file):
    dictionnary = {}
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        compteur = 0
        for row in csv_reader:
            string_list = [row[1], row[2], row[3], row[4], row[5], row[6]]
            dictionnary[row[0]] = [int(stat) for stat in string_list]
            compteur += 1
    return dictionnary

pkmn = charger_pokemon_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
