from person import human

class employee(human):

    def __init__(self):

        self.__position = ''
        self.__salary = 0

    @property
    def getSalary(self):
        return self.__salary
    @property 
    def getPosition(self):
        return self.__position


    def createEmployee(self):

        super().createHuman()
        self.__position = input('Enter position : ')
        self.__salary = int(input('Enter salary : '))

    def showData(self):

        super().showData()
        print(f'Salary : {self.__salary}\nPosition : {self.__position}\n--------------------------')