# Course: CMIT235
# Assignment 2-4
# Date: 3/28/2021, 4/4/2021, 4/10/2021
# Name: Michael Tofteland
# Description: A2 - This project creates a class, instantiates an object in MyTest.py, and calls methods on that object.
# Description: A3 - This project extends NetworkCheck with getters, reading a data dump, iterating over packets, and
# getting private variables
# Description A4 - This project uses overloaded methods to parse data from a CSV file and overrides a method from the
# NetworkCheck Parent Class to alter the calculations performed on the existing numpy Array
# Description A5 - This project utilizes inheritance to expand on existing class methods to further analyze network
# traffic.

import numpy as np
import pandas as pd
from scapy.layers.inet import UDP, TCP
from scapy.layers.l2 import Ether

import CMIT235_Tools as cm
from multipledispatch import dispatch


class NetworkCheck:

    def __init__(self):
        self.__spoofed_mac_count = 0
        self.__port_count = 0
        self.__message1 = "Welcome to message 1"
        self._message2 = "Welcome to message 2"
        self.message3 = "Welcome to message 3"

    #
    # Week 2 Methods
    #

    def convertList2NpArray(self, myList):
        newNpArray = np.array(myList)
        return newNpArray

    def getMax(self, newNpArray):
        return np.max(newNpArray)

    def getMin(self, newNpArray):
        return np.min(newNpArray)

    def getUniqueValues(self, newNpArray):
        return np.unique(newNpArray)

    def getDescriptiveInfo(self, myList):
        myDict = {}
        count = 1
        for i in myList:
            arr1 = np.array(i)
            strCount = str(count)
            myDict["Dimension" + strCount] = arr1.ndim
            myDict["Shape" + strCount] = arr1.shape
            myDict["LastItem" + strCount] = arr1[1, -1]
            myDict["Column0" + strCount] = arr1[0:, 0]
            myDict["SecondRow" + strCount] = arr1[1:]
            count += 1
        return myDict

    #
    # Week 3 Methods
    #

    # Return private message 1
    def getMessage1(self):
        return self.__message1

    # Return protected message 2
    def getMessage2(self):
        return self._message2

    # Return spoofed MAC count
    def getSpoofedMacCount(self, packets, mac):
        try:
            for packet in packets:
                if packet[Ether].src == mac:
                    self.__spoofed_mac_count += 1
        except:
            print("Unable to get MAC count")
        return self.__spoofed_mac_count

    # Return port count
    def getPortCount(self, packets, port):
        try:
            for packet in packets:
                if packet.haslayer(UDP) or packet.haslayer(TCP):
                    if packet.dport == port:
                        self.__port_count += 1
        except:
            print("Unable to get port count")
        return self.__port_count

    #
    # Week 4 Methods
    #

    @dispatch(str, str)
    def checkCounts(self, df, feature):
        # Read csv
        df = pd.read_csv(cm.csv_data)
        # Return unique value count for "feature"
        return df[feature].value_counts()

    @dispatch(str, str, str, str)
    def checkCounts(self, df, feature1, feature2, feature3):
        # Read csv
        df = pd.read_csv(cm.csv_data)
        # Create dictionary
        dfDict = {}
        dfDict[feature1] = df[feature1].value_counts()
        dfDict[feature2] = df[feature2].value_counts()
        dfDict[feature3] = df[feature3].value_counts()
        # Return Dictionary of feature1, feature2, and feature3
        return dfDict

    @dispatch(str, str, str, str, str, str)
    def checkCounts(self, df, feature1, feature2, feature3, feature4, feature5):
        # Read csv
        df = pd.read_csv(cm.csv_data)
        largest = df.groupby([feature1, feature2, feature3, feature4, feature5]).size().nlargest(1)
        return largest
