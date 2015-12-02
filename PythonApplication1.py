import timeit

from Ar import *
from Domain import*


def printTimePass(stop, start):
    s = stop - start
    m = int(s / 60.0)
    print("Time Elapsed: {:d}m {:.5}s".format(m, s))


print ("we will run: send more money| please edit wordList in the python application to change")
print("some puzzles may take longer")

wordList = ["tiles","puzzles","picture"]
wordList = ["send","more","money"]

# copy to a tmp list.
tmpList = list(wordList)

# CSP setup.
var1 = extractSep(tmpList)[0] # extract char
cList = setConstDict(tmpList)
var4 = extractChars(tmpList)
dMap = setDomainTable(extractChars(tmpList), tmpList)


# Print the Domain.
print("---Domain---")
for name in dMap:
    print(dMap[name])
print("------------\n")


# Start the timer. 
start = timeit.default_timer()
# Run the CSP.
isOkay = setWithMostConst(cList, dMap, tmpList)
# Stop the timer.
stop = timeit.default_timer()


# print some output. 
if isOkay:
    print("\nCSP Pass!!\n")
    
    for i in range(len(wordList)):
    
        if i == len(wordList) -1:
            print("----------  ----------")
    
        print("{:>10} {:>11}".format(wordList[i], wordToNum(tmpList[i], dMap)))
    
    print("\n")
    printTimePass(stop, start)

else:
    print("CSP Fail!!")
