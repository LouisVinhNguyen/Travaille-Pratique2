import csv
import json

with open("data.json", 'r') as data_json:
    complexe_liste = json.load(data_json)

with open("data.csv", "w", newline='') as data_csv:
    data_csv_writer = csv.writer(data_csv, delimiter=",")
    data_csv_writer.writerow(["reel", "imaginaire"])
    for nombre in complexe_liste:
        data_csv_writer.writerow([nombre[0], nombre[1]])