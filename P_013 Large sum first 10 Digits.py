import re

file_object = open("problem13.txt")
numbers_array = [int(re.sub('[^0-9]', '', line)) for line in file_object]

print str(sum(numbers_array))[:10]

