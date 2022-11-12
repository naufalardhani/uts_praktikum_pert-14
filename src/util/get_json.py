import json

def getDataFromJsonFile(file):
    with open(file, "r") as connect:
        return json.load(connect)