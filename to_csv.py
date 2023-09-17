from helpers import utils
import json
import os

#Create folder to store the csv files
path = utils.SAVE_LOC + "/csv"
if not os.path.exists(path):
    os.makedirs(path)

#Function to load data from json file
def load_json(name: str) -> dict:
    with open(utils.SAVE_LOC + "/json/" + name, "r") as file:
        return json.load(file)
    
#Function to save the csv file
def save_csv(data: list[dict], name: str):
    import csv
    with open(path + "/" + name + ".csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

#Read files in json folder
files = os.listdir(utils.SAVE_LOC + "/json")

for file in files:
    print(f"Loading data from {file}... ", end="")
    data = load_json(file)
    print("Done")

    print(f"Saving data to {file}... ", end="")
    save_csv(data, file.removesuffix(".json"))
    print("Done", end="\n\n")
