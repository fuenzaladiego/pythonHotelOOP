class human():

    def __init__(
        self):
        self.__name = ''
        self.__age = 0
        self.__nationaliy = ''

    def createHuman(
            self):
        self.__name = input('Enter name : ')
        self.__age = int(input('Enter age : '))
        self.__nationaliy = input("Enter country of origin : ")
        

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getNationality(self):
        return self.__nationaliy

    def setAge(self,age):
        self.__age = age

    def setName(self,name):
        self.__name = name
    
    def setNationality(self,nationality):
        self.__nationaliy = nationality

    def showData(self):
        print(f'--------------------------\nNombre : {self.__name}\nEdad : {self.__age}\nPais de origen : {self.__nationaliy}')

