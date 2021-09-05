import json

def getData(file):
    jsonFile = open(file, "r")
    return json.loads(jsonFile.read())
