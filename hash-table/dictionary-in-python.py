d = {'name': 'Kevin', 'age': 34, 'gender': 'male'}

print(d.keys())
print(d.values())

print(d['name'])
print(d['age'])
print(d['gender'])

print('---------')

for key, value in d.items():
    print(key, value)

d.clear()
print(d.keys())
print(d.values())

# delete dictionary
# del d