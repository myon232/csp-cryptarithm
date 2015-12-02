from Ar import *
from Domain import*
print ("we will run: send more money| please edit mylist in the python application to change")
print("some puzzles may take longer")

mylist = ["tiles","puzzles","picture"]




var1 = extractSep(mylist)[0]#extract char
cList = setConstDict(mylist)
var4 = extractChars(mylist)
dMap = setDomainTable(extractChars(mylist),mylist)
for name in dMap:
    print(dMap[name])



setWithMostConst(cList,dMap,mylist)

print("tiles","puzzles","picture")
for word in mylist:
    print(wordToNum(word,dMap))