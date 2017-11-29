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
    test_getInitials()



def test_getInitials():
    fullName = "John Samuel Wobbly"
    part = fullName.lower().title()

    msg = ''
    for i in part:
        if i.isupper():
            msg += i

    print "The initials of John Samuel Wobbly are", msg



    fullName = "Dylan McDermott"
    part = fullName.lower().title()

    msg = ''
    for i in part:
        if i.isupper():
            msg += i

    print "The initials of Dylan McDermott are", msg

    fullName = "Nora Young"
    part = fullName.lower().title()

    msg = ''
    for i in part:
        if i.isupper():
            msg += i

    print "The initials of Nora Young are", msg


if __name__ == '__main__':
    main()
