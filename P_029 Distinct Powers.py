result_set = set()

for i in range(2, 101):
    for j in range(2, 101):
        result_set.add(i**j)

print(len(result_set))
