

def main():
    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    if fcName.endswith("_PLY"):
        return "Polygon"
    elif fcName.endswith("_ply"):
        return "Polygon"
    elif fcName.endswith("_LIN"):
        return "Line"
    elif fcName.endswith("_lin"):
        return "Line"
    elif fcName.endswith("_PNT"):
        return "Point"
    elif fcName.endswith("_pnt"):
        return "Point"
    else:
        print"Unknown."

def test_getFeatureTypeFromName():
    #Test for Polygon Upper
    fcName= "Provinces_PLY"
    expected="Polygon"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Polygon"
    #Test for Polygon Lower
    fcName= "Provinces_ply"
    expected="Polygon"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Polygon"
    #Test for Line Upper
    fcName= "Provinces_LIN"
    expected="Line"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Line"
    #Test for Line Lower
    fcName= "Provinces_lin"
    expected="Line"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Line"
    #Test for Point Upper
    fcName= "Provinces_PNT"
    expected="Point"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Point"
    #Test for Point Lower
    fcName= "Provinces_pnt"
    expected="Point"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Point"
    #Test for Else(Improper Naming)
    fcName= "Provinces_Lin"
    expected="Line"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Line"
    #Test for Else(No Underscore)
    fcName= "ProvincesLIN"
    expected="Line"
    actual = getFeatureTypeFromName(fcName)
    if expected == actual:
        print "Line"


if __name__ == '__main__':
    main()