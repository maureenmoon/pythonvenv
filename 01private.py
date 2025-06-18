class Patient:
    def __init__(self,name):
        self.name = name #public
        self.__temp = 36.5 #접근제어자

    def set_temp(self,temp): #변경값일 경우 set
        if 35 <= temp <= 38:
            self.__temp = temp
            print(f'temp {temp} is normal')
        else:
            print('temp is abnormal')

    def get_temp(self): #접근제어자 항상 만들어야함
        return self.__temp
    
name=input('input name')
patient = Patient(name) #instance 생성

try:
    temp = float(input('input temperature'))
    patient.set_temp(temp)
except ValueError:
    print('temp is invalid. input in a number format')

print(f'{patient.name} current temperature is {patient.get_temp()}')

        