# This problem is from FiveThirtyEight.com's weekly riddle
# http://fivethirtyeight.com/features/what-if-robots-cut-your-pizza/

import random    

def do_intersect(slice1, slice2):
    if (slice1[0] < slice2[0]):
        first = slice1
        second = slice2
    else:
        first = slice2
        second = slice1
    return first[1] > second[0] and first[1] < second[1]

def count_intersections(slices):
    intersections = 0
    for i in xrange(len(slices)):
        for j in xrange(i+1, len(slices)):
            if do_intersect(slices[i], slices[j]):
                intersections += 1
    return intersections

sliceCount = 3
iterations = 10000000
resultCount = {}
for iteration in xrange(iterations):
    slices = []
    for i in xrange(sliceCount):
        a = random.random()
        b = random.random()
        if a<b:
            sliceTup = (a,b)
        else:
            sliceTup = (b,a)
        slices.append(sliceTup)
    intersections = count_intersections(slices)
    if intersections in resultCount:
        resultCount[intersections] += 1
    else:
        resultCount[intersections] = 1

print resultCount
expectedValue = 0
for intersections in resultCount:
    expectedValue += 1.0 * resultCount[intersections] / iterations * (sliceCount + intersections + 1)
print expectedValue


