# Course: CMIT235
# Assignment 4
# Date: 4/10/2021 - 4/30/2021
# Name: Michael Tofteland
# Description A4 - This project uses overloaded methods to parse data from a CSV file and overrides a method from the
# NetworkCheck Parent Class to alter the calculations performed on the existing numpy Array
#
# Description A7 - This project utilizes advanced functions to increase functionality of existing code.

import numpy as np
from NetworkCheck import NetworkCheck


# Inherit NewNetworkCheck from NetworkCheck Parent Class
class NewNetworkCheck(NetworkCheck):

    def __init__(self):
        super().__init__()

    def getDescriptiveInfo(self, myList):
        myDict = {}
        count = 1
        for i in myList:
            arr1 = np.array(i)
            strCount = str(count)
            myDict["Dimension" + strCount] = arr1.ndim
            myDict["Shape" + strCount] = arr1.shape
            myDict["Mean" + strCount] = np.mean(arr1)
            myDict["Median" + strCount] = np.median(arr1)
            myDict["SD" + strCount] = np.std(arr1)
            count += 1
        return myDict

    def callSuper(self, newNpArray):
        superMin = super().getMin(NetworkCheck, newNpArray)
        print(f'The new min is: {superMin}')
