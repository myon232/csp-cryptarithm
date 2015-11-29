class Variable:
    """description of class"""
    def __init__(self, name, id):
        self.name = name
        self.domain = [0,1,2,3,4,5,6,7,8,9]
        self.id = id
        self.value = -1
        
    def print(self):
        print(self.name)
        print(self.domain)
        print(self.id)
        print(self.value)
       

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.id, self.domain, self.value)


def setVar(varName, varValue, varMap):
    
    for v in varMap:
        
        if varName == varMap[v].name:
            varMap[v].value = varValue
        
        varMap[v].domain.remove(varValue)


def unsetVar(varName, varMap):
    
    varValue = varMap[varName].value
    
    if varValue > -1 and varValue < 10:
        
        for v in varMap:
            
            if varValue not in varMap[v].domain:
                varMap[v].domain.append(varValue)
    
    varMap[varName].value = -1
