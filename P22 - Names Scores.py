
import csv

def get_name_score(name):
    score = 0
    for x in list(name):
        score += (ord(x.lower()) - 96)
    return score

names_array = []
with open('p_22_names.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        for name in row:
            names_array.append(name)

sorted_names_array = sorted(names_array)

score = 0
for index, name in enumerate(sorted_names_array, start = 1):

    score += (index * get_name_score(name))
    print index,name,get_name_score(name), score