from Domain import*

def appendString(string):
	stringArray = []
	stringArray.append(string)
	return stringArray

def extractChars(stringArray):
	charSet = set()
	for word in stringArray:
		for letter in word:
			charSet.add(letter)
	return charSet 

def extractSep(wordList):
	lastChars = set()
	charSet = set()
	for word in wordList[:-1]:
		for letter in word:
			charSet.add(letter)
			#add carries here

	for letter in wordList[-1]:
		lastChars.add(letter)

	return lastChars, charSet

def setConstDict(wordList):
    constDict = {}
    lastWord = wordList[-1][::-1]
    rWordList = reverseWordList(wordList)
    
    for column in range(0, len(lastWord)):
        constDict[lastWord[column]] = getColumn(column, rWordList)
        #constDict[lastWord[column]].append('x'+str(column))    
    return constDict

def reverseWordList(wordList):
	for indx, word in enumerate(wordList):
		wordList[indx] = word[::-1]
		
	return wordList

def getMaxWordLength(wordList):
	lengthList = []
	for word in wordList:
		lengthList.append(len(word))
	return max(lengthList)

def getColumn(columnNum, wordList):
	columnArray  = []
	for word in wordList[:-1]:
		if columnNum <len(word):
			columnArray.append(word[columnNum])
	return columnArray

def setDomainTable(letters,wordList):
    domainTable = {}
    
    # Adding just vars.
    for name in letters:
        domainTable[name] = Variable(name,1)
    
    '''
    # Adding carry vars.
    for i in range(0,getMaxWordLength(wordList)):
        var = Variable('x'+str(i),2)
        var.domain.clear()
        var.domain = [0,1]
        domainTable['x' + str(i)] = var
        # print(domainTable[name])# domains are set
    '''
    
    return domainTable

def removeFromDomain(domainTable,domainID, number):
     for name in domainTable:
         if domainTable[name].id == domainID:
             for num in domainTable[name].domain:
                if number == num:
                    domainTable[name].domain.pop(number)
            # print(domainTable[name]) # a number has been removed from the domain
     return domainTable

def addToDomain(domainTable,domainID, number):
    for name in domainTable:
        if domainTable[name].id == domainID:
            domainTable[name].domain.append(number)
            domainTable[name].domain.sort()
    return domainTable;

def setDomain(domainTable,letter,number):
        for name in domainTable:
            if letter == name:
                domainTable[name].value = number
                if domainTable[name].id <= 1:
                    removeFromDomain(domainTable,domainTable[name].id,number)
        return domainTable
#def mostConst(constTable):



def getVarValue(domainTable, varName):
    
    for letter in domainTable:
        if domainTable[letter].name == varName:
            return domainTable[letter].value
            
    return -2#error not found

def getDomain(domainTable,constTable, variable):
    for key in domainTable:
        if key == variable:
            smallerDomain = []
            for vv in domainTable[key].domain:
                if testVarValue(domainTable,constTable, variable, vv):
                    smallerDomain.append(vv)
                    
            return smallerDomain
    return []

def getRight(rightVar, domainTable):
    varValue = getVarValue(domainTable, rightVar)
    if varValue < 0:
        return -1;
    return varValue

def getLeft(leftList, domainTable):

    valueList = []

    for varName in leftList:
        varValue = getVarValue(domainTable, varName)
        if varValue < 0:
            return -1
        valueList.append(varValue)

    return sum(valueList);


def testVarValue(domainTable,constTable,variable, testValue):

    isValueGood = True

    for cKey in constTable:
        if cKey == variable or variable in constTable[cKey]:
            sumRight = getRight(cKey, domainTable)
            sumLeft = getLeft(constTable[cKey], domainTable)
            
            if sumLeft < 0 or sumRight < 0:
                continue
            elif sumRight != sumLeft and sumRight +10 !=sumLeft and sumRight != sumLeft +1 and sumRight +10 != sumLeft +1:
                isValueGood = False
                break

    return isValueGood

def isCarryVariable(variable):
    return "x" in variable

def forwardCheck(domainTable,constTable):
    for var in constTable:
        if len(constTable[var]) ==  1 and "x" in constTable[var] :
            domainTable = setVar(var, 1, domainTable)
    return domainTable

def computeConst(constTable, domainTable):
    sumMap = {}
    for ckey in constTable:
        cList =  constTable[ckey]
        tmpSumList =[]
        listIsGood = True
        print(cList)


        for item in cList:
            value = getVarValue(domainTable, item)
            if(value > -1 ):
             tmpSumList.append(value)
             
            else:
                print("{}=>{}".format(item, value))
                listIsGood = False
                break
        if(listIsGood):
           sumMap[ckey] = sum(tmpSumList)
        else:
            sumMap[ckey] = -1 

    return sumMap

def getMaxConst(domainTable):
    minlen = 0
    
    maxKey = ''
    
    for key in domainTable:
        if minlen < len(domainTable[key].domain) and  domainTable[key].value < 0:
            minlen = len(domainTable[key].domain)
            maxKey = key
    return maxKey
    

def isSet(domainTable):
    N = True
    for key in domainTable:
        if domainTable[key].value < 0:
            N =  False
            break        
    return N

def wordToNum(word, domainTable):
    
    stack = ""
    for letter in word:
        value = getVarValue(domainTable, letter)

        if value < 0 or value > 10:
            return -1

        stack += str(value)
    
    return int(stack[::-1])



def setWithMostConst(constTable,domainTable,wordList):
    
    if isSet(domainTable) == False:
        domainTable = forwardCheck(domainTable,constTable) 
        maxKey = getMaxConst(domainTable)
        for value in getDomain(domainTable,constTable, maxKey):
            
            setVar(maxKey, value, domainTable)
            
            if setWithMostConst(constTable,domainTable,wordList):
                return True
               
            unsetVar(maxKey, domainTable)
            

    else:
        
        
        solve = []
        for word in wordList:
            solve.append(wordToNum(word, domainTable))
        if sum(solve[:-1]) == solve[-1]:
            print("Here is your output Prof:")
            
            for varKey in domainTable:
                print("{} -> {}".format(varKey, domainTable[varKey].value))
            
            return True
    
    return False
