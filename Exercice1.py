import csv
import json

data_list = [[2, 3], [3, 2], [1.0, -5.3]]

with open("data.json", "w") as data_json:
    json.dump(data_list, data_json, indent=4)

with open("data.json", 'r') as data_json:
    tuples_list = json.load(data_json)

with open("data.csv", "w") as data_csv:
    data_csv_writer = csv.writer(data_csv, delimiter=",")
    data_csv_writer.writerow(["reel", "imaginaire"])
    for tuple in tuples_list:
        data_csv_writer.writerow([tuple[0], tuple[1]])



