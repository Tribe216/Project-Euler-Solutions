#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bhm7
#
# Created:     06/01/2014
# Copyright:   (c) bhm7 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pyramid_vec = []
    file_object = open("problem67.txt")
    for line in file_object:
        pyramid_vec.append(list(map(int,line.split())))

    for i in range(len(pyramid_vec)-1,-1,-1):
        current_row = pyramid_vec[i]
        for j in range(0,len(current_row)-1):
            pyramid_vec[i-1][j] = pyramid_vec[i-1][j] + max(current_row[j], current_row[j+1])
    print pyramid_vec[0][0]

if __name__ == '__main__':
    main()
