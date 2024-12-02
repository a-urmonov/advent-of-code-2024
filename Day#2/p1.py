with open("input2.txt", "r") as file:
    data = file.readlines()

safe_count = 0
unsafe_count = 0
reports = []
for line in data:
    values = line.split()
    val_int = [int(x) for x in values]
    reports.append(val_int)

for levels in reports:
    for idx in range(len(levels)-1):
        if (1<=abs(levels[idx]-levels[idx+1])<=3) and ((sorted(levels)==levels) or (sorted(levels, reverse=True)==levels)):
            continue
        else:
            unsafe_count += 1
            break

# print(safe_count)
# print(unsafe_count)
print(len(reports)-558)
