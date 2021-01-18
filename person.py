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
        
    @property
    def getName(self):
        return self.__name
    @property
    def getAge(self):
        return self.__age
    @property
    def getNationality(self):
        return self.__nationaliy

    def showData(self):
        print(f'--------------------------\nNombre : {self.__name}\nEdad : {self.__age}\nPais de origen : {self.__nationaliy}')

