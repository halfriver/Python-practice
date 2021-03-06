'''
Problem 9 - Mean Median Mode
- Create three functions that allow the user to find the mean, median, and mode
of a list of numbers. If you have access to or know of functions that already
complete these tasks, do not use them - create them from scratch!
- In the mean function, give the user a way to select how many decimal places
they want the answer to be rounded to.
- If there is an even number of numbers in the list, return both numbers that
could be considered the median.
- If there are multiple modes, return all of them. If there is not one, say so.
'''

# Original: 10 Sept 2019
# Edited: 25 November 2020

import math
from collections import Counter


def mean(numlist, decimals):
    # new function, return
    return round(sum(numlist)/len(numlist), decimals)


''' ORIGINAL
    mean = 0
    for x in range(0, len(num)):
        mean += num[x]
    mean /= len(num)
    return float(mean)
'''


def median(numlist):
    # new function, returns list of 1 or 2 integers
    numlist = sorted(numlist)
    # if number of list items is even, return both numbers at the median
    if len(numlist) % 2 == 0:
        # if both median numbers are the same, only report one
        if numlist[len(numlist)//2] == numlist[(len(numlist)//2)+1]:
            return [numlist[len(numlist)//2]]
        else:
            return [numlist[len(numlist)//2], numlist[(len(numlist)//2)+1]]
    # if number of list items is odd, return the one median
    else:
        return [numlist[(len(numlist)-1)//2]]


''' ORIGINAL
    median = 0
    if len(num) % 2 == 0:
        x = math.ceil(len(num)/2)
        y = x - 1
        median = float((num[x] + num[y])/2)
        return median
    else:
        median = num[math.floor(len(num)/2)]
        return median
'''


def mode(numlist):
    # new function, returns dictionary
    # keeps track of max frequency
    mcount = 0
    # keeps track of (max frequency: mode(s))
    mdict = {}
    # creates dictionary of items in numlist and the frequency of each
    counter = Counter(numlist)
    for x in counter:
        # if item in list has frequency greater than max, set it equal to max
        if counter[x] > mcount:
            mcount = counter[x]
            mdict = {mcount: [x]}
        # if equal to max, include it in dictionary of modes
        elif counter[x] == mcount:
            mdict[mcount].append(x)
    if len(counter) == len(mdict[mcount]):
        return ""
    else:
        return mdict


''' ORIGINAL
    mode_count = 1
    mode = []
    for x in range(0, len(num)):
        if num.count(num[x]) > mode_count:
            mode_count = num.count(num[x])
            mode = [num[x]]
        elif num.count(num[x]) == mode_count and num[x] not in mode:
            mode.append(num[x])
    return (mode, mode_count)
'''

# check that input list is more than one integer
num = [x for x in input("Provide a list of numbers separated by commas.\n").replace(" ", "").split(",")]
while True:
    if len(num) <= 1:
        num = [x for x in input("Please enter more than one number. Make sure that there are commas separating your input.\n").replace(" ", "").split(",")]
    else:
        try:
            num = [int(x) for x in num]
            break
        except ValueError:
            num = [x for x in input("Please make sure that you are entering integers.\n").replace(" ", "").split(",")]

# ask how many decimal places the mean should have; make sure it's an int
deci = input("How many decimal places should we round the mean to?\n").replace(" ", "")
while True:
    try:
        deci = int(deci)
        break
    except ValueError:
        deci = input("Please input a single integer.\n").replace(" ", "")

# print mean
print("Mean: " + str(mean(num, deci)))

# print median
med = ""
for x in median(num):
    med += str(x)
    if x != median(num)[len(median(num))-1]:
        med += ", "
print("Median(s): " + med)

# print mode
mod = ""
freq = ""
if mode(num) == "":
    print("Mode(s): NA")
else:
    for x in mode(num):
        freq = str(x)
        for y in mode(num)[x]:
            mod += str(y)
            if y != mode(num)[x][len(mode(num)[x])-1]:
                mod += ", "
    print("Mode(s): " + mod + ", which occurs " + freq + " times")
