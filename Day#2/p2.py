with open("input2.txt", "r") as file:
    data = file.readlines()

safe_count = 0
unsafe_count = 0
reports = []
unsafe_reports = []
for line in data:
    values = line.split()
    val_int = [int(x) for x in values]
    reports.append(val_int)

for levels in reports:
    for idx in range(len(levels)-1):
        if (1<=abs(levels[idx]-levels[idx+1])<=3) and ((sorted(levels)==levels) or (sorted(levels, reverse=True)==levels)):
            continue
        else:
            unsafe_reports.append(levels)
            unsafe_count += 1
            break

def safety_check(levels):
    for idx in range(len(levels)-1):
        if (1<=abs(levels[idx]-levels[idx+1])<=3) and ((sorted(levels)==levels) or (sorted(levels, reverse=True)==levels)):
            continue
        else:
            return False
    return True

new_count = 0
for levels in unsafe_reports:
    # print(levels)
    for index in range(len(levels)):
        n = levels[:index] + levels[index+1:]
        # print(n)
        if safety_check(n) == True:
            new_count += 1
            break
        # print(safety_check(n))

print(new_count+442)
# print(unsafe_reports)
# print(len(unsafe_reports))
