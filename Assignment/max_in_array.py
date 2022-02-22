
arr = [125, 101, 720, 15, 456, 221, 312]
max = arr[0]
for i in range(0, len(arr)):
    if arr[i] > max:
        max = arr[i]
print("Largest element present in given array: " + str(max));