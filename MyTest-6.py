# Course: CMIT235
# Assignment 1-7
# Date: 3/21/2021 - 4/30/2021
# Name: Michael Tofteland
# Description: This project combines and manipulates data from external files.

import numpy as np
from scapy.all import *
import logging

from CMIT235_Package import CMIT235_Tools as cm
from CMIT235_Package.AddedNetworkCheck import AddedNetworkCheck
from CMIT235_Package.NetworkCheck import NetworkCheck
from CMIT235_Package.NewNetworkCheck import NewNetworkCheck

# Week 6 - Log file and info statement

logging.basicConfig(filename='CMIT235_MyTest.log', level=logging.DEBUG)

logging.info('Begin log')

# Week 1 Assignment

# Week 6.1 Error handling #1
print("Assignment 6.1:")

if not type(cm.mySubList1 or cm.mySubList2 or cm.mySubList3) is list:
    print("SubLists of myList must be of type list")
    logging.error("MyTest TypeError at line 27. Sublists must be of type list.")
    sys.exit(1)
else:
    print("Combining sublists of type lists...\n")

# End Week 6.1 Error handling #1

# Concatenate subLists and print.
myList = [cm.mySubList1] + [cm.mySubList2] + [cm.mySubList3]

print("ASSIGNMENT 1 OUTPUT\n\nThe list of values is:\n", myList)

# Week 6.2 Error handling #2
print("\nAssignment 6.2:\nConverting to numpy array...")

try:
    # Convert to numpy array.
    myNpArray = np.array(myList)
except ValueError:
    print("SubLists of myList must be of type list")
    logging.error("MyTest ValueError at line 44. Incorrect Value.")
    sys.exit(2)
except TypeError:
    print("SubLists of myList must be of type list")
    logging.error("MyTest TypeError at line 44. Incorrect Type.")
    sys.exit(3)

# End Week 6.2 Error handling #2

# Week 6.3 Error handling #3
print("\nAssignment 6.3:\nCalculating minimum...")

if np.min(myNpArray) < 100:
    # Print lowest value.
    print("The lowest value is:", np.min(myNpArray))
else:
    raise Exception("The minimum is greater than 100!")

# End Week 6.3 Error handling #3

# Week 6.4 Error handling #4
print("\nAssignment 6.4:\nCalculating maximum...")

if np.max(myNpArray) > 0:
    # Print highest value.
    print("The highest value is:", np.max(myNpArray))
else:
    raise Exception("The max is less than 0!")

# End Week 6.4 Error handling #4

# Week 6.5 Error handling #5
print("\nAssignment 6.5:\nFinding unique values...")

if not type(np.unique(myNpArray)) is np.ndarray:
    print("UniqueValues of myList must be of type NDARRAY")
    logging.error("MyTest TypeError at line 83. UniqueValues must be of type NDARRAY.")
    sys.exit(4)
else:
    # Print unique values.
    print("The unique list is:\n", np.unique(myNpArray))

# End Week 6.5 Error handling #5

# Week 6.6 Error handling #6
print("\nAssignment 6.6:\nAssessing types...")

for subList in myList:

    if not type(np.array(subList)) is np.ndarray:
        print("SubLists must be of type NDARRAY")
        logging.error("MyTest TypeError at line 98. SubLists must be of type NDARRAY.")
        sys.exit(5)
    else:
        print("\nThe sublist is of type NDARRAY")

# End Week 6.6 Error handling #6

    # Create NumPy array from each sublist.
    myNpArraySubList = np.array(subList)

    # Print each NpArraySubList within myList.
    print("\nThe sublist is:\n", myNpArraySubList)

    # Print dimension quantity of NpArraySubList.
    print("\nThe quantity of dimensions for this sublist is:", myNpArraySubList.ndim)

    # Print shape of NpArraySubList.
    print("The shape of this sublist is:", myNpArraySubList.shape)

    # Print sliced first row of the NpArraySubList.
    print("The slice of the first row of this sublist is:\n", myNpArraySubList[0, 0:12])

    # Print last number in the slice of the NpArraySubList.
    print("The last number in the slice is:", myNpArraySubList[0, 11])

    # Print the first numbers in each row of the NpArraySubList.
    print("The values in column 0 for this sublist are:", myNpArraySubList[0:2, 0])

    # Print the sliced second row of the NpArraySubList.
    print("The second row in this sublist is:\n", myNpArraySubList[1, 0:12])


# Week 2 Assignment

# Week 6 - NetworkCheck info statement
logging.info('Begin NetworkCheck log')

# Instantiate NetworkCheck Class
myNetworkCheck = NetworkCheck()

# Week 6.7 Error handling #7
print("\nAssignment 6.7:\nValidating myNetworkCheck object...")

try:
    isinstance(myNetworkCheck, NetworkCheck)
    print("myNetworkCheck is an instance of class NetworkCheck.")
except ValueError:
    print("myNetworkCheck is not an instance of class NetworkCheck!")
    sys.exit(6)

# End Week 6.7 Error handling #7

# Convert list to numpy array
newNpArray = myNetworkCheck.convertList2NpArray(myList)

# End Week 6.8 Error handling #8
print("\nAssignment 6.8:\nCalculating minimum...")

# Call getMin method to get lowest value
listMin = myNetworkCheck.getMin(newNpArray)

if listMin < 100:
    print("The minimum is less than 100.")
else:
    raise Exception("The minimum is greater than 100!")

# End Week 6.8 Error handling #8

# Week 6.9 Error handling #9
print("\nAssignment 6.9:\nCalculating maximum...")

# Call getMax method to get highest value
listMax = myNetworkCheck.getMax(newNpArray)

if listMax > 0:
    print("The highest value greater than 0")
else:
    raise Exception("The max is less than 0!")

# End Week 6.9 Error handling #9

# Week 6.10 Error handling #10
print("\nAssignment 6.10:\nChecking unique value type...")

# Call getUniqueValues method to show each unique value
unique = myNetworkCheck.getUniqueValues(myList)

if not type(unique) is np.ndarray:
        print("UniqueValues must be of type NDARRAY")
        logging.error("MyTest TypeError at line 187. UniqueValues must be of type NDARRAY.")
        sys.exit(7)
else:
    print("The UniqueValues is of type NDARRAY")

# End Week 6.10 Error handling #10

# Week 6.11 Error handling #11
print("\nAssignment 6.11:\nChecking description type...")

# Call getDescriptiveInfo method
description = myNetworkCheck.getDescriptiveInfo(myList)

if not type(description) is dict:
    raise Exception("Description must be of type dict!")
else:
    print("Description is of type dict.")

# End Week 6.11 Error handling #11

# Print values of all methods
print("\n\nASSIGNMENT 2 OUTPUT\n\nThe list of values for Object myNetworkCheck is:\n", newNpArray)
print("\nThe highest value in the list of values for Object myNetworkCheck is:", listMax)
print("\nThe lowest value in the list of values for Object myNetworkCheck is:", listMin)
print("\nThe unique values in the list of values for Object myNetworkCheck are:\n", unique)
print("\nThe descriptive info for the sublists for Object myNetworkCheck is:\n", description)


# Week 3 Assignment

print("\n\nASSIGNMENT 3 OUTPUT\n")

# Private message 1
try:
    print(myNetworkCheck.message1())
except:
    print("Cannot get message 1")
print(myNetworkCheck.getMessage1())

# Protected message 2
try:
    print(myNetworkCheck.message2())
except:
    print("\nCannot get message 2")
print(myNetworkCheck.getMessage2())

# Public message 3
print("\n" + myNetworkCheck.message3)

# Print message 1, message 2, and message 3
print(f"\n{myNetworkCheck.getMessage1():>25}{myNetworkCheck.getMessage1():>25}{myNetworkCheck.message3:>25}\n")

# Week 6.12 Error handling #12
print("\nAssignment 6.12:\nChecking packets capture file...")

# Read pcap
packets = rdpcap(cm.pcap)

try:
    open(cm.pcap)
    print("Packets capture file is open.\n")
except Scapy_Exception:
    print("Error opening packets capture file!\n")
    sys.exit(8)

# End Week 6.12 Error handling #12

# Week 6.13 Error handling #13
print("\nAssignment 6.13:\nChecking mac count type...")

#Get the spoofed mac count
mac_count = myNetworkCheck.getSpoofedMacCount(packets, cm.spoofed_mac)

if not type(mac_count) is int:
    print("mac_count is not of type int!\n")
    sys.exit(9)
else:
    print("mac_count is of type int.\n")

# End Week 6.13 Error handling #13

print("-----------------------Spoofed MAC Count is----------------------------")
print("The spoofed MAC count is", mac_count)

# Week 6.14 Error handling #14
print("\nAssignment 6.14:\nChecking port count type...")

# Get the port 135 count
port_count = myNetworkCheck.getPortCount(packets, cm.port)

if not type(port_count) is int:
    print("port_count is not of type int!\n")
    sys.exit(10)
else:
    print("port_count is of type int.\n")

# End Week 6.14 Error handling #14

print("-----------------------Port 135 count is-------------------------------")
print("The port count for", cm.port, "is", port_count)


# Week 4 Assignment

print("\n\nASSIGNMENT 4 OUTPUT\n")

# Week 6.15 Error handling #15
print("\nAssignment 6.15:\nValidating protocol count...")

# Call overloaded methods
check1 = myNetworkCheck.checkCounts(cm.csv_data, cm.feature3)

try:
    print(f"The counts of unique values for {cm.feature3} are:\n", check1)
except ValueError:
    print("Error encountered in count validation!")
    sys.exit(11)

# End Week 6.15 Error handling #15

# Week 6.16 Error handling #16
print("\nAssignment 6.16:\nValidating check2 type...")

check2 = myNetworkCheck.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3)

if not type(check2) is dict:
    raise Exception("check2 must be of type dict!")
else:
    print("check2 is of type dict.")
    print(f"\nThe counts of unique values for {cm.feature1}  are:\n", check2[cm.feature1])
    print(f"\nThe counts of unique values for {cm.feature2} are:\n", check2[cm.feature2])

# End Week 6.16 Error handling #16

# Week 6.16 Error handling #16
print("\nAssignment 6.16:\nValidating check3...")

check3 = myNetworkCheck.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3, cm.feature4, cm.feature5)

try:
    print("\n\nThe elements with the largest count value for each feature are:\n", check3)
except ValueError:
    print("Error encountered in count validation!")
    sys.exit(12)

# End Week 6.16 Error handling #16

# Instantiate myNewNetworkCheck Object to call overridden method
myNewNetworkCheck = NewNetworkCheck()

# Week 6.17 Error handling #17
print("\nAssignment 6.17:\nValidating myNewNetworkCheck object...")

try:
    isinstance(myNewNetworkCheck, NewNetworkCheck)
    print("myNewNetworkCheck is an instance of class NewNetworkCheck.")
except ValueError:
    print("myNewNetworkCheck is not an instance of class NewNetworkCheck!")
    logging.DEBUG("Instantiation of NewNetworkCheck unsuccessful.")

# End Week 6.17 Error handling #17

# Call getDescriptiveInfo method from NewNetworkCheck Class
newDescription = myNewNetworkCheck.getDescriptiveInfo(myList)
print("\nThe descriptive info for the sublists for Object myNewNetworkCheck is:")
for key, value in newDescription.items():
    print(key, " : ", value)


# Week 5 Assignment

print("\n\nASSIGNMENT 5 OUTPUT\n")

# 5.1 Demonstrate calling methods from parent

# Declare Variables
# Convert list to numpy array
newNetworkCheckNpArray = myNewNetworkCheck.convertList2NpArray(myList)
# Call getMax method to get highest value
newMax = myNewNetworkCheck.getMax(newNetworkCheckNpArray)
# Call getMin method to get lowest value
newMin = myNewNetworkCheck.getMin(newNetworkCheckNpArray)
# Call getUniqueValues method to show each unique value
newUnique = myNetworkCheck.getUniqueValues(myList)

# Call NetworkCheck methods to check Inheritance
print("The list of values for Object myNewNetworkCheck is:\n", newNetworkCheckNpArray)
print("\nThe highest value in the list of values for Object myNewNetworkCheck is:", newMax)
print("\nThe lowest value in the list of values for Object myNewNetworkCheck is:", newMin)
print("\nThe unique values in the list of values for Object myNewNetworkCheck are:\n", newUnique)

# 5.2 Demonstrate extending child class by calling method that exists in child class but not in its parent class.

# Instantiate myAddedNetworkCheck Object to call methods including those inherited from superclasses
myAddedNetworkCheck = AddedNetworkCheck()

# Week 6.18 Error handling #18
print("\nAssignment 6.18:\nValidating myAddedNetworkCheck object...")

try:
    isinstance(myAddedNetworkCheck, AddedNetworkCheck)
    print("myAddedNetworkCheck is an instance of class AddedNetworkCheck.")
except ValueError:
    print("myAddedNetworkCheck is not an instance of class AddedNetworkCheck!")
    logging.INFO("Instantiation of AddedNetworkCheck unsuccessful.")

# End Week 6.18 Error handling #18

# 5.3 Demonstrate multiple layers of inheritance by having a grandchild call a method of its grandparent.

# Call getSpoofedMacCount method
new_mac_count = myAddedNetworkCheck.getSpoofedMacCount(packets, cm.spoofed_mac)
print("\n-----------------------Spoofed MAC Count is----------------------------")
print("The spoofed MAC count is", new_mac_count)

# Call getPingCount method
ping_count = myAddedNetworkCheck.getPingCount(packets, cm.window)
print("\n--------------------------Ping Count is--------------------------------")
print("The count for TCP packet window 65535 is: ", ping_count)

# Call checkCounts method using feature3
new_check = myAddedNetworkCheck.checkCounts(cm.csv_data, cm.feature3)
print(f"\nThe counts of unique values for {cm.feature3} are:\n", new_check)


# Assignment 7

print("\nAssignment 7.1:\nCalling parent's getMin method from child via super()...")

# Convert sublist to np array
subList2NpArray = myNetworkCheck.convertList2NpArray(cm.mySubList2)

# Print minimum
print(NewNetworkCheck.callSuper(NewNetworkCheck, subList2NpArray))

print("\nAssignment 7.2:\nVerifying subclass status using issubclass lambda...")

x = lambda child, parent: issubclass(child, parent)

try:
    x(NewNetworkCheck, NetworkCheck) == True
    print("NewNetworkCheck is a subclass of NetworkCheck.")
except ValueError:
    print("Error: NewNetworkCheck is a subclass of NetworkCheck!")
    logging.DEBUG("Subclass verification of NewNetworkClass unsuccessful.")
    sys.exit(13)

print("\nAssignment 7.3:\nCalling grandparent's getMax method from grandchild via super()...")

# Convert sublist to np array
subList3NpArray = myNetworkCheck.convertList2NpArray(cm.mySubList3)

# Print maximum
print(AddedNetworkCheck.callGrandparent(AddedNetworkCheck, subList3NpArray))

print("\nAssignment 7.4:\nVerifying subclass status using issubclass lambda...")

try:
    x(AddedNetworkCheck, NewNetworkCheck) == True
    print("AddedNetworkCheck is a subclass of NewNetworkCheck.")
except TypeError:
    print("Error: AddedNetworkCheck is a subclass of NewNetworkCheck!")
    logging.DEBUG("Subclass verification of AddedNetworkClass unsuccessful.")
    sys.exit(14)

print("\nAssignment 7.5:\nExecuting repeat method...")


def repeat(mySubList):
    # stop condition
    if len(mySubList) == 1:
        return mySubList
    # rescursive function
    else:
        half = len(mySubList)//2
        firstList = mySubList[:half]
        secondList = mySubList[half:]
        return repeat(firstList), repeat(secondList)


z = repeat(cm.mySubList1[0])
print("The recursively parsed list is:")
print(z)