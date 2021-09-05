import json

jsonFile = open("Automat_Epsilon.json", "r")
data = json.loads(jsonFile.read())

""" for node in data["Nodes"]:
    print(node)

print("\n")

print(data["Nodes"][0]) """
del data["Nodes"][0]

print("\n")

for node in data["Nodes"]:
    print(node)

print("\n")
A = "Q10"
B = "QQQ"
C = "Q11"
addNode = {
    "Start": f"{A}",
    "Cond": f"{B}",
    "End": f"{C}"
}

data["Nodes"].insert(0, addNode)

for node in data["Nodes"]:
    print(node)
