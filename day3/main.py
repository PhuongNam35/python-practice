import json

with open("input.json", "r") as file:
    data = json.load(file)

# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)

print(f"{data} \n")

for key, value in data.items():
    print(f"{key}: {value}")
