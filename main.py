import time
from cal_ans import getAns

while True:
    user_input = input("Find Expression for result 10\n(To exit enter q)\nINPUT NUMBERS : ")
    if ("q" in user_input) or ("ㅂ" in user_input):
        break

    calStartTime = time.time()
    ans = getAns(user_input)
    calEndTime = time.time()

    execTime = str(calEndTime-calStartTime)
    print("ANSWER IS  " + ans + "\n(calculation time : " + execTime + " sec)" + "\n\n")