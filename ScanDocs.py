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
    test_getPatternPosition()



def hasXcode(inText):
    if inText.find('Tx6op3') != -1:
        return True
    else:
        return False

def test_hasXcode():
    #True Case
    inText = "dajkdhasTx6op3asjkdh"
    expected = True
    actual = hasXcode(inText)
    if expected == actual:
        print "The code was found in the text."

    else:
        print fmt.format(expected,actual)

    #False Case
    inText = "dajkdhasT6op3asjkdh"
    expected = False
    actual = hasXcode(inText)
    if expected == actual:
        print "The code was not found in the text."

    else:
        print fmt.format(expected,actual)


def getXcodePosition(inText):
    if inText.find("Tx6op3") == -1:
        return False

    else:
        return True

def test_getXcodePosition():
    #True Case
    inText = "dajkdhasTx6op3asjkdh"
    expected = True
    actual = getXcodePosition(inText)
    if expected == actual:
        print "The code was found in the text at position ", inText.find("Tx6op3")+1

    else:
        print fmt.format(expected,actual)

    #False Case
    inText = "dajkdhasT6op3asjkdh"
    expected = False
    actual = getXcodePosition(inText)
    if expected == actual:
        print -1, "(The code was not found.)"

    else:
        print fmt.format(expected,actual)

def getPatternPosition(pattern,inText):
    if inText.find(pattern) == -1:
        return False

    else:
        return True

def test_getPatternPosition():
    #True Case
    inText = "sdajhTx6op3aSLKDJ"
    pattern = "3aSLK"
    expected = True
    actual = getPatternPosition(pattern,inText)
    if expected == actual:
        print "The code was found in the text at position ", inText.find(pattern)+1

    else:
        print fmt.format(expected,actual)

    #False Case
    inText = "sdajhTx6op3aSKDJ"
    pattern = "3aSLK"
    expected = False
    actual = getPatternPosition(pattern,inText)
    if expected == actual:
        print -1, "(the code was not found.)"

    else:
        print fmt.format(expected,actual)



if __name__ == '__main__':
    main()
