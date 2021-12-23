# Course: CMIT235
# Assignment 5
# Date: 4/17/2021 - 4/30/2021
# Name: Michael Tofteland
# Description A5 - This class inherits from NewNetworkCheck and adds getPingCount functionality.
#
# Description A7 - This project utilizes advanced functions to increase functionality of existing code.

import numpy as np
from scapy.layers.inet import TCP

from CMIT235_Package.NewNetworkCheck import NewNetworkCheck
from CMIT235_Package.NetworkCheck import NetworkCheck


# Inherit AddedNetworkCheck from NewNetworkCheck Parent Class
class AddedNetworkCheck(NewNetworkCheck):

    def __init__(self):
        NewNetworkCheck.__init__(self)
        self.__ping_count = 0

    # Return packets with TCP layer and window property of 65536
    def getPingCount(self, packets, window):
        try:
            for packet in packets:
                if packet.haslayer(TCP):
                    if packet[TCP].window == 65535:
                        self.__ping_count += 1
        except:
            print("Unable to get ping count")
        return self.__ping_count

    def callGrandparent(self, newNpArray):
        superMax = super().getMax(NetworkCheck, newNpArray)
        print(f'The new max is: {superMax}')

    # def repeat(self, mySubList):
    #     # stop condition
    #     if len(mySubList) == 1:
    #         return mySubList
    #     # rescursive function
    #     else:
    #         half = len(mySubList)//2
    #         repeat([mySubList[:half], mySubList[half:]])
    #
    #
    # def repeat(self, mySubList):
    #         # stop condition
    #         if len(mySubList) == 1:
    #             return mySubList
    #         # rescursive function
    #         else:
    #             half = len(mySubList)//2
    #             repeat([mySubList[:half], mySubList[half:]])
