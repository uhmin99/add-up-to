from itertools import product, permutations, combinations

BASIC_OPERATORS = ["+","-","*","/"]

def getAns(uInput: str, operators="") :
    # Set usable operators
    OPERATORS = []
    if operators == "": OPERATORS = BASIC_OPERATORS
    else : OPERATORS = makeOpCodable(operators)

    inputNumList = uInput.split(" ")

    # Insert math operators between the numbers
    for numList in permutations(inputNumList, inputNumList.__len__()):
        for i in product(OPERATORS, repeat=numList.__len__() - 1) :
            exp = ""

            # make expression for calculation
            for j in range(numList.__len__()):
                if j==numList.__len__()-1:
                    exp += numList[j]
                else:
                    exp += (numList[j]+i[j])

            # test expression
            expRes = getExpResult(exp)
            if expRes == 10 :
                resultExp = makeOpReadable(exp)
                return resultExp
            else :
                # Try exp with Bracket
                for numIndexComb in combinations(list(range(numList.__len__())),2):
                    expWithBracket = ""
                    if numIndexComb == (0, numList.__len__()-1):
                        continue
                    
                    for k in range(numList.__len__()):
                        toBeAdded = ""
                        numString = ""
                        if k==numIndexComb[0]:
                            numString += ("("+numList[k])
                        elif k==numIndexComb[1]:
                            numString += (numList[k]+")")
                        else :
                            numString += numList[k]
                        
                        if k==numList.__len__()-1:
                            toBeAdded = numString
                        else :
                            toBeAdded = numString+i[k]

                        expWithBracket += toBeAdded
                    
                    expBracketRes = getExpResult(expWithBracket)

                    if expBracketRes == 10:
                        resultExpWithBracket = makeOpReadable(expWithBracket)
                        return resultExpWithBracket
                        
                            

    return "SOLUTION NOT FOUND"
    

def getExpResult(expression: str):
    try:
        if "/0" in expression :
            return -1
        
        result = eval(expression)

        if (type(result) is int) or (type(result) is float) :
            return result
        else :
            print("!!NON NUMBER TYPE DETECTED!!" + str(result))
            return -1
    except:
        # print("ERROR : exception happened in getting getExpResult\nError exp is " + expression)
        return -1
    

def makeOpReadable(exp: str):
    replaceMul = exp.replace("*", "X")
    resultExp = replaceMul.replace("/", "÷")
    return resultExp

def makeOpCodable(ops: str):
    devideReplaced = ops.replace("÷", "/")
    codableOps = devideReplaced.replace("X", "*")
    opsList = codableOps.split(" ")

    return opsList