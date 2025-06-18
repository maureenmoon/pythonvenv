
#constructor  생성자 만들기
#클래스 안의 함수 = 메서드 = 행동을 취함
#getter: 값을 가져올때
#setter: 값을 변경할때

class Account:
    # def __init__(self, amount):

    # def __init__(self):
    #     self.balance = 10000
    #     self.name = 'hongGD'

    def __init__(self, name, amount):
        self.balance = amount

    def deposit(self,amount): #위의 amount와 다른 것이다
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

# hong = Account(10) # 초기값 #함수 실행 
# hong = Account("HongGD",10) # 초기값 #함수 실행 
# print(hong.deposit(1000))

# hong = Account("Hong",10000) #init value
# value=hong.deposit(1000)
# print(f'current balance of {hong.name} is {value}')

class Account1:
    def __init__(self,name='',amount=0):
        self.name = name #public
        self.__balance = amount #private attribute
        
    def deposit(self,amount):
        self.__balance +=amount
        return self.__balance
    
    def withdraw(self,amount):
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance
    
# a1 = Account1('hongGD')
# print(f'{a1.name}-saving account balance : {a1__balance}')

# a1=Account1()
# a1.name = 'Lee'

a1 = Account1('leeGD',10000)
a1.deposit(540)
print(f'{a1.name}-saving account balance : {a1.get_balance()}')
    
