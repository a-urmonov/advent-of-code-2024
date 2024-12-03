import re
with open("input3.txt", "r") as file:
    data = file.readlines()

corrupted = []
for line in data:
    values = line.split()
    corrupted.append(line)

pattern = r"(do\(\)|don't|mul\(\s*\d+\s*,\s*\d+\s*\))"

results = []
for string in corrupted:
    matches = re.findall(pattern, string)
    results.append(matches)

pattern2 = r"mul\((\d+),(\d+)\)"


res2 = []
for item in results:
    for i in item:
        res2.append(i)

# print(res2)

result = []
skip_numbers = False
for match in res2:
    if match == "don't": 
        skip_numbers = True
    elif match == "do()":  
        skip_numbers = False
    else:
        if not skip_numbers:
            result.append(match)

# print(result)


pattern2 = r"mul\((\d+),(\d+)\)"
number_tuples = [(int(x), int(y)) for x, y in re.findall(pattern2, ' '.join(result))]
# print(number_tuples)

t = 0
for item in number_tuples:
    t += item[0]*item[1]
print(t)
