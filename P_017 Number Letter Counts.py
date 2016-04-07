from time import clock

start_time = clock()

ones = {\
0 : '',\
1 : 'one',\
2 : 'two',\
3 : 'three',\
4 : 'four',\
5 : 'five',\
6 : 'six',\
7 : 'seven',\
8 : 'eight',\
9 : 'nine'\
}

teens = {\
0 : 'ten',\
1 : 'eleven',\
2 : 'twelve',\
3 : 'thirteen',\
4 : 'fourteen',\
5 : 'fifteen',\
6 : 'sixteen',\
7 : 'seventeen',\
8 : 'eighteen',\
9 : 'nineteen'\
}

tens = {\
0 : '',
2 : 'twenty',\
3 : 'thirty',\
4 : 'forty',\
5 : 'fifty',\
6 : 'sixty',\
7 : 'seventy',\
8 : 'eighty',\
9 : 'ninety'\
}

def to_words(number):
    ret_string = ""
    num_array = list(map(int,list(str(number).zfill(4))))
    if num_array[0]:
        ret_string = ret_string + ones[num_array[0]] + "thousand"

    if num_array[1]:
        ret_string = ret_string + ones[num_array[1]] + "hundred"

    if num_array[2] or num_array[3]:
        if num_array[0] or num_array[1]:
            ret_string= ret_string + "and"

        if num_array[2] == 1:
            ret_string = ret_string + teens[num_array[3]]
        elif num_array[2] != 1:
            ret_string = ret_string + tens[num_array[2]] + ones[num_array[3]]

    return ret_string
abs

char_counter = 0
for i in range(1,1001):
    char_counter += len(to_words(i))

print char_counter
print clock() - start_time, "seconds"