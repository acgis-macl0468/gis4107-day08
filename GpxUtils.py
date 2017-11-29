#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jake MacLean
#
# Created:     29-11-2017
# Copyright:   (c) Jake MacLean 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def main():
    test_getCoordsFromGpx()

def getCoordsFromGpx(gpx):
    if gpx.startswith("<trkpt"):
        return "Yes"

    else:
        print "None."



def test_getCoordsFromGpx():
    #True Test
    gpx = """<trkpt lat="45.3888995" lon="-75.7472631">"""
    expected = "Yes"
    actual = getCoordsFromGpx(gpx)
    if expected == actual:
        import re
        gp = map(int, re.findall('\d+', gpx))
        print '(','-',gp[2],'.',gp[3],',',gp[0],'.',gp[1],')'

    #False Test
    gpx = """<kpt lat="45.3888995" lon="-75.7472631">"""
    expected = "Yes"
    actual = getCoordsFromGpx(gpx)
    if expected == actual:
        import re
        gp = map(int, re.findall('\d+', gpx))
        print '(','-',gp[2],'.',gp[3],',',gp[0],'.',gp[1],')'





if __name__ == '__main__':
    main()
