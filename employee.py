from person import human

class employee(human):

    def __init__(self):

        self.__position = ''
        self.__salary = 0


    def getSalary(self):
        return self.__salary

    def getPosition(self):
        return self.__position

    def setSalary(self,salaryy):
        self.__salary = salaryy

    def setPosition(self,position):
        self.__position = position

    def createEmployee(self):

        super().createHuman()
        self.__position = input('Enter position : ')
        self.__salary = int(input('Enter salary : '))
        print('\n')

    def showData(self):

        super().showData()
        print(f'Salary : {self.__salary}\nPosition : {self.__position}\n--------------------------')