def maximumUnitsTruck(boxTypes, truckSize):
    #sort arr to maximize units, therefore sort in descending order of units
    boxTypes.sort(key = lambda x: x[1], reverse=True)
    totalUnits = 0
    for box, units in boxTypes:
        if box <= truckSize:
            totalUnits += (box * units)
            truckSize -= box
        else:
            totalUnits += (truckSize * units)
            return totalUnits
    return totalUnits         


print(maximumUnitsTruck([[5,10],[2,5],[4,7],[3,9]],truckSize=10))    