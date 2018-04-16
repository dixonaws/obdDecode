import json


def main():
    print "obdDecode v1.0"
    print "Decode hex values into their integer equivalent and encode into JSON"
    print "Intended to be deployed to Greengrass Core to decode hex messages from a:freeRTOS"

    strObdPids = "aaaa9e0000003600000034580000a900" \
                 "0000b50000000000000000000000000000" \
                 "0000000000000000000000000000000000" \
                 "0000000000000000000000000000000000" \
                 "0000000000000000000000000000000000" \
                 "0000000000000000000000000000000000" \
                 "0000000000000000000000000000000000" \
                 "000000000000000000000000aaaa";

    # strObdPids should contain the following PIDs
    # 4 - engine load
    # 10 - fuel pressure
    # 12 - engine rpm
    # 13 - vehicle speed
    # 17 - throttle position

    # see: https://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_01 for more info on decoding logic

    intObdPidsLength = len(strObdPids)

    # strip off the first four and last four characters
    strObdPids = strObdPids[4:intObdPidsLength - 4]

    print "Input message: " + strObdPids

    lstPids = []

    i = 0
    intPidNumber = 1
    while i < intObdPidsLength:
        strPid = strObdPids[i:i + 8]
        lstPids.append(strPid)
        i = i + 8
        intPidNumber += 1

    for pid in lstPids:
        print pid

    lstPidPosition = []
    lstPidPosition.insert(0, 'EngineLoad')  # PID=4
    lstPidPosition.insert(1, 'FuelPressure')  # PID=10
    lstPidPosition.insert(2, 'EngineRPM')  # PID=12
    lstPidPosition.insert(3, 'VehicleSpeed')  # PID=13
    lstPidPosition.insert(4, 'ThrottlePosition')  # PID=17

    print "Engine RPM per calculation is " + str(calculateEngineRPM(lstPids[lstPidPosition.index('EngineRPM')]))

    print "Engine load per calculation is " + str(calculateEngineRPM(lstPids[lstPidPosition.index('EngineLoad')]))

    # print "The engine load value in hex is " + lstPids[lstPidPosition.index('EngineLoad')]
    # print "The fuel pressure value in hex is " + lstPids[lstPidPosition.index('FuelPressure')]
    # print "The throttle position value in hex is " + lstPids[lstPidPosition.index('ThrottlePosition')]

    # from the a:freeRTOS program to query PIDs from the neoOBD2Pro
    # pidNumberLookup[32] =
    # {4, 10, 12, 13, 17, 35, 47, 48,
    #  49, 77, 92, 93, 94, 98, 99, 100,
    #  101, 102, 16, 18, 19, 20, 21, 22,
    #  23, 24, 25, 26, 27, 28, 29, 30};

def calculateEngineRPM(hexEngineRPM):
    # raw hex, not yet decoded
    hexEngineRPM_A = hexEngineRPM[0:4]
    hexEngineRPM_B = hexEngineRPM[4:8]

    # convert to base10
    intEngineRPM_A = int(hexEngineRPM_A, 16)
    intEngineRPM_B = int(hexEngineRPM_B, 16)

    # calculation on mode 1 PIDs for engine RPM: =A/4 + B/4
    intEngineRPM = (intEngineRPM_A / 4) + (intEngineRPM_B / 4)

    return intEngineRPM

def calculateEngineLoad(hexEngineLoad):
    # calculation on mode 1 PIDs for engine load: A(100/255)

    hexEngineLoad_A = hexEngineLoad[0:4]

    # convert to base10
    intEngineLoad_A = int(hexEngineLoad_A, 16)

    intEngineLoad=intEngineLoad_A(100/255)

    return intEngineLoad

main()
