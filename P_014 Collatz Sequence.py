from time import clock

def coll_chain(input):
    current_num = input
    counter = 0
    coll_string = ""
    while current_num > 1:

        #coll_string += str(current_num) + "_"
        counter+=1

        if (current_num % 2) == 0:
            current_num = current_num / 2
        else:
            current_num = (3*current_num) + 1
    return counter

start_time = clock()
largest_chain_yet = 0

for i in range(1000000):
    if coll_chain(i) > largest_chain_yet:
        largest_chain_yet  = coll_chain(i)
        largest_i = i

print largest_i
print clock() - start_time, "seconds"