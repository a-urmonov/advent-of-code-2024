# example_list_left = [3,4,2,1,3,3]
# example_list_right = [4,3,5,3,9,3]

with open("input1.txt", "r") as file:
    data = file.readlines()

column_left = []
column_right = []
for line in data:
    values = line.split()
    column_left.append(int(values[0]))
    column_right.append(int(values[1]))


def duplicate_count(arr, num):
    count = 0
    for i in arr:
        if num == i:
            count += 1 
    return count

# x = duplicate_count(example_list_right, num=1)
# print(x)
similarity_score = 0
for j in column_left:
    c = duplicate_count(column_right, num=j)
    similarity_score += c*j

print(similarity_score)
