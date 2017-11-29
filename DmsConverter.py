#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jake MacLean
#
# Created:     28-11-2017
# Copyright:   (c) Jake MacLean 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def getEW(dmsRecord):
    print dmsRecord.upper()
    return dmsRecord.upper()

def getNS(dmsRecord):
    print dmsRecord.upper()
    return dmsRecord.upper()

def dms2dd(dmsRecord):
    record = dmsRecord.split()
    EW = getEW(record[3])
    NS = getNS(record[7])
    if record[0].isdigit() :
        print record[0]
    if record[4].isdigit() :
        print record[4]
    if record[5].isdigit():
        print record[5]
    if record[6].isdigit():
        print record[6]
    if record[2].isdigit():
        print record[2]
    if record[1].isdigit():
        print record[1]
    print record

dms2dd("007 45 03 W 45 23 05 N\n")

if __name__ == '__main__':
    main()
