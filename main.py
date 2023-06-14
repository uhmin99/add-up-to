import time
from cal_ans import getAns

print("Find Expression for result 10!!\n\n\n")
while True:
    input_ops = input("Is there any operation limits?\n(To exit enter q)\nEnter Usable Ops(Press Enter if all Operators are available) : ")
    if ("q" in input_ops) or ("ㅂ" in input_ops):
        break

    input_nums = input("\nINPUT NUMBERS(seperate them by a space) : ")
    if ("q" in input_nums) or ("ㅂ" in input_nums):
        break

    calStartTime = time.time()
    ans = getAns(input_nums, input_ops)
    calEndTime = time.time()

    execTime = str(calEndTime-calStartTime)
    print("ANSWER IS  " + ans + "\n(calculation time : " + execTime + " sec)" + "\n\n")