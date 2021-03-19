array = [10, 3, 7, 5]

print(array)


# this is called random indexing: indexes starts with 0
print("random indexing:", array[2])

print(array[0:2])


# this is called linear search O(N)
max = array[0]

for num in array:
    if num > max:
        max = num

print(max)
