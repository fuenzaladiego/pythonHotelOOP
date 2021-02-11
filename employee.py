from person import human

class employee(human):

    def __init__(self):

        self.__position = ''
        self.__salary = 0
        self.__id = -1


    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getSalary(self):
        return self.__salary

    def getPosition(self):
        return self.__position

    def setSalary(self,salaryy):
        self.__salary = salaryy

    def setPosition(self,position):
        self.__position = position

    def createEmployee(self,id):

        super().createHuman()
        self.__position = input('Enter position : ')
        self.__salary = int(input('Enter salary : '))
        self.__id = id
        print('\n')

    def modifyEmployee(self,position,salary,name,nation,age):

        if len(position) > 0:
            self.setPosition(position)
        if salary > 0: 
            self.setSalary(salary)

        if len(name) > 0:
            self.setName(name)

        if len(nation) > 0:
            self.setNationality(nation)

        if age > 0:
            self.setAge(age)


    def showData(self):

        super().showData()
        print(f'Salary : {self.__salary}\nPosition : {self.__position}\nId : {self.__id}\n--------------------------')