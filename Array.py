array = [10, 3, 7, 5]

print(array[2])


max = array[0]

for num in array:
    if num < max:
        max = num

print(max)
