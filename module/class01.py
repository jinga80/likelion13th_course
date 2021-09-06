class Cal:
    def __init__(self, result=0):
        print("객체생성")
        self.result = result
    
    def plus(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result


#클래스 객체
c1 = Cal()

#클래스 메서드 실행
c1.plus(20)

print(c1.result)