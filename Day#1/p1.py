
with open("input1.txt", "r") as file:
    data = file.readlines()

column_left = []
column_right = []
for line in data:
    values = line.split()
    column_left.append(int(values[0]))
    column_right.append(int(values[1]))

# print(len(column_left))

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)


def partition(arr, left, right):
    i = left 
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j: 
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i


# test case 
# arr = [3,5,1,9,2,0,-1,4,2]
length = len(column_left)
quicksort(column_left, 0, length-1)
quicksort(column_right, 0, length-1)

s = 0
for i in range(0,length):
    s += abs(column_left[i] - column_right[i])
print(s)