import random


#사칙연산 클래스 만들기



def cal(op, num1, num2):
    if op=="+":
        print("두 값의 합은 : ", num1+num2)
    elif(op=='-'):
        print("두 값의 차는 : ", num1-num2)


#두값을 입력받기



a = int(input("값1 :"))
b = int(input("값2 :"))

cal("+",a,b)