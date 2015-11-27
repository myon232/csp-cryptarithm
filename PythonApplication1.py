from Ar import *
from Domain import*
print ("This is the beginning of your first python program rae")
mylist = ["two", "two", "four"]

#print(extractChars(mylist))

var1 = extractSep(mylist)[0]#extract char
var2 = setConstDict(mylist)
var = setDomainTable(extractChars(mylist))

print("this is a message stop fucking up yo")
Dtable = removeFromDomain(var, 0)
for name in Dtable:
    print (Dtable[name])
print("end testing")

print(var2)


""" now I can now remove numbers from a domain. so lets walk threw this.

1. I want to set the variable with the variable with the smallest number of contraints
    to do this i will look at my constraint variables at and set the first one to one, the second one to two 
    then three(or the next variable in the domain)
    1. set to a number in domain
    2. remove number from all domains in domain
    3. continue to the next Letter in dict, and loop and set
    4. if their is a fail x-- (step back)
taking a think break 
#for myVar in var:
 #   print(myVar)
#dict1 = setConstDict(var1,mylist)#set dictionary

#print(extractSep(mylist))

#print(reverseWordList(mylist))

#print(getMaxWordLength(mylist))

#print(getColumn(3,mylist))"""