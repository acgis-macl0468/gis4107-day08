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

def isValidPhoneNumber(phoneNumber):
    phoneNumber = '613-950-9999'
    if len(phoneNumber) !=12:
        return False
    for x in range(0,3):
        if phoneNumber().isdecimal():
            return False
    if phoneNumber[3] !='-':
        return False
    for x in range(4,7):
        if not text[i].isdecimal():
            return False
    if phoneNumber[7] != '-':
        return False
    for x in range(8,12):
        if not phoneNumber[i].isdecimal():
            return False
    return True

print '613-950-9999 is a valid phone number:'
print isValidPhoneNumber(613-950-9999)
print 'Hello-world is a phone number:'
print isValidPhoneNumber('Hello-world')

# phoneNumber = NNN-NNN-NNNN
if __name__ == '__main__':
    main()
