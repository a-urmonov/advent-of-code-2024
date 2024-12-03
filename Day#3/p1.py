import re
with open("input3.txt", "r") as file:
    data = file.readlines()

corrupted = []
for line in data:
    values = line.split()
    corrupted.append(line)

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

results = []
for string in corrupted:
    matches = re.findall(pattern, string)
    products = [int(x) * int(y) for x, y in matches]
    results.extend(products)

s = 0
for i in results:
    s += i 

print(s)




