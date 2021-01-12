import itertools

first = itertools.combinations(flower_names, 1)

for i in first:
    print(i)

second = itertools.combinations(flower_names, 2)

for i in second:
    print(i)

third = itertools.combinations(flower_names, 3)

for i in third:
    print(i)
