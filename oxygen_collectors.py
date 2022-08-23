oxygenCollect = 1.5 #Amount of oxygen collected per second per leaf block.
maxRange = 11 * 11 * 11 #Size of maximum leaf block cube.

collectors = 0 #How many collectors there are.
leaves = 0 #The amount of leaves.
oxygenTotal = 0
oxygenTotalMax = 0 #How many .


while True:
    leaves = maxRange - collectors #More collectors mean less leaves to make room.
    oxygenTotal = oxygenCollect * leaves * collectors
    if oxygenTotal > oxygenTotalMax:
        oxygenTotalMax = oxygenTotal
    collectors = collectors + 1
    if collectors == maxRange:
        oxygenTotalMax = str(oxygenTotalMax)
        collectors = str(collectors)
        print("The optimal amount of collectors are " + collectors + ", which will produce " + oxygenTotalMax + " units of oxygen per second.")
        break