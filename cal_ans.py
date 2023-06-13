from itertools import product, permutations

OPERATORS = ["+","-","*","/"]

def getAns(uInput: str) :
    inputNumList = uInput.split(" ")
    # 각 숫자 사이에 사칙연산 넣기
    for numList in permutations(inputNumList, inputNumList.__len__()):
        for i in product(OPERATORS, repeat=numList.__len__() - 1) :
            exp = ""

            # make expression for calculation
            for j in range(numList.__len__()):
                if j==numList.__len__()-1:
                    exp += numList[j]
                else:
                    exp += (numList[j]+i[j])

            # test exp
            expRes = getExpResult(exp)
            if expRes == 10 :
                resultExp = makeOpReadable(exp)
                return resultExp
            # else :
            #     testWithBlank(exp)
            #     # 만들어진 식에 괄호 넣어보기

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
        print("ERROR : exception happened in getting getExpResult")
        return -1
    

def makeOpReadable(exp: str):
    replaceMul = exp.replace("*", "X")
    resultExp = replaceMul.replace("/", "÷")
    return resultExp