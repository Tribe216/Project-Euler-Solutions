#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 11
# Purpose:
#
# Author:      bhm7
#
# Created:     18/12/2013
# Copyright:   (c) bhm7 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def get_product(numbers_array):
    best_p = [0,0,0,""]
    for x in range(20):
        for y in range(20):

            if(y < 17):
                p_down = reduce( lambda x,y: x*y, [ numbers_array[x][y+z] for z in range(4) ] )
                if p_down > best_p[0]:
                    best_p = p_down,x,y,"down"
                print x,y,numbers_array[x][y],"down", p_down

            if(x < 17):
                p_right = reduce( lambda x,y: x*y, [ numbers_array[x+z][y] for z in range(4) ] )
                if p_right > best_p[0]:
                    best_p = p_right,x,y,"right"
                print x,y,numbers_array[x][y],"right", p_right

            if(x < 17 and y < 17):
                p_diag_rd = reduce( lambda x,y: x*y, [ numbers_array[x+z][y+z] for z in range(4) ] )
                if p_diag_rd  > best_p[0]:
                    best_p = p_diag_rd ,x,y,"diag_rd"
                print x,y,numbers_array[x][y],"diag_rd", p_diag_rd

            if(x < 17 and y > 2):
                p_diag_ru = reduce( lambda x,y: x*y, [ numbers_array[x+z][y-z] for z in range(4) ] )
                if p_diag_ru > best_p[0]:
                    best_p = p_diag_ru,x,y,"diag_ru"
                print x,y,numbers_array[x][y],"diag_ru", p_diag_ru

            print "*******"

    return best_p



file_object = open("problem11.txt")
number_array = [[0 for x in xrange(20)] for x in xrange(20)]
pivoted_array = [[0 for x in xrange(20)] for x in xrange(20)]

for i in range (20):
    number_array[i] = file_object.readline().split()

for x in range(20):
        for y in range(20):
            pivoted_array[x][y] = int(number_array[y][x])
result = get_product(pivoted_array)
print result[0],"at x,y",result[1],result[2],"direction:",result[3]