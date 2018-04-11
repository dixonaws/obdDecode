import json

def main():
    print "obdDecode v1.0"
    print "Decode hex values into their integer equivalent and encode into JSON"
    print "Intended to be deployed to Greengrass Core to decode hex messages from a:freeRTOS"

    strObdPids="aaaa9e0000003600000034580000a900" \
               "0000b50000000000000000000000000000" \
               "0000000000000000000000000000000000" \
               "0000000000000000000000000000000000" \
               "0000000000000000000000000000000000" \
               "0000000000000000000000000000000000" \
               "0000000000000000000000000000000000" \
               "000000000000000000000000aaaa";

    print "Input message: " + strObdPids

    # strObdPids should contain the following PIDs
    # 4 - engine load
    # 10 - fuel pressure
    # 12 - engine rpm
    # 13 - vehicle speed
    # 17 - throttle position

    # see: https://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_01 for more info on decoding logic

    intObdPidsLength=len(strObdPids)
    lstPids=[]

    i=0
    intPidNumber=1
    while i<intObdPidsLength:
        strPid=strObdPids[i:i+8]
        lstPids.append(strPid)
        i=i+8
        intPidNumber+=1

    # we need to remove the 'aaaa' records from the list as they only represent
    # the start and end of the string
    # lstPids.pop(lstPids.index('aaaa'))
    # lstPids.pop(lstPids.index('aaaa'))

    for pid in lstPids:
        print pid

    lstPidPosition=[]
    lstPidPosition.insert(0, 'EngineLoad')
    lstPidPosition.insert(1, 'FuelPressure')
    lstPidPosition.insert(2, 'EngineRPM')

    # raw hex, not yet decoded
    print "The engine RPM value in hex is " + lstPids[lstPidPosition.index('EngineRPM')]

    # from the a:freeRTOS program to query PIDs from the neoOBD2Pro
    # pidNumberLookup[32] =
    # {4, 10, 12, 13, 17, 35, 47, 48,
    #  49, 77, 92, 93, 94, 98, 99, 100,
    #  101, 102, 16, 18, 19, 20, 21, 22,
    #  23, 24, 25, 26, 27, 28, 29, 30};


main()
