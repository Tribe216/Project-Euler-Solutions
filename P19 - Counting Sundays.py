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

import datetime

def main():
    counter = 0

    for year_iter in range (1901,2001):
        for month_iter in range (1,13):
            if datetime.date(year_iter,month_iter,1).weekday() == 6:
                counter += 1
    print counter
if __name__ == '__main__':
    main()
