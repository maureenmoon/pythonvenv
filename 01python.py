# print("test")

balance  = 0
balance2=0

def deposit(amount): # amount= 매개변수
    # balance = 1000
    global balance # 함수 외부에 선언된 balance를 함수내에서 사용하게 하는 
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

def deposit2(amount): # amount= 매개변수
    # balance = 1000
    global balance2 # 함수 외부에 선언된 balance를 함수내에서 사용하게 하는 
    balance2 += amount
    return balance2

def withdraw2(amount):
    global balance2
    balance2 -= amount
    return balance2

print("cash-in",deposit(1000))
print("cash-out",withdraw(500))
print("account balance",balance)

print("cash-in",deposit2(2000))
print("cash-out",withdraw2(400))
print("account balance",balance2)


class Account:
    def __init__(self):
        self.balance = 0 #inital constructor 만듬 , 속성 초기화
        
    def deposit(self, amount): #메서드
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

hong = Account() #객체 생성
print("hong's cash-in",hong.deposit(1000))
print("hong's cash-out",hong.withdraw(754))
print("hong's balance",hong.balance)
print('---'*10)

moon = Account()
print("moon's cash-in",moon.deposit(2000))
print("moon's cash-out",moon.withdraw(333))
