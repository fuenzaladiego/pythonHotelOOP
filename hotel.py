from employee import *
from room import *
from customer import *





def validateNumber(dicionary,number):
    length = len(dicionary)
    if length == 0:
        return True
    else:
        for x in dicionary:
            if x == number:
                print('Number already in use.\n')
                return False
        return True
    
    return False

def validateLength(length):

    if length > 0:
        return True
    else:
        return False

    
    


class hotel():

    def __init__(self):

        self.__hotelName = input('Enter the hotel name : ')
        print('\nEnter the manager info : ')
        self.__rooms = {}
        self.__employees = {}

        self.__hotelManager = employee()
        self.__hotelManager.createEmployee(1)
        self.__employees[1] = self.__hotelManager
         
        


    def getHotelManager(self):
        return self.__hotelManager

    def getHotelName(self):
        return self.__hotelName
    
    def setHotelName(self,name):
        self.__hotelName = name
    
    def setHotelManager(self,manager):
        self.__hotelManager = manager
    
    def deleteHotelManager(self):
        self.__hotelManager = None
    
    
        



    def managerInfo(self):
        manager = self.getHotelManager()
        print('Manager info\n')
        manager.showData()

    
    
    def showRooms(self):
        length = len(self.__rooms)
        print(f'Total number of rooms : {length}\n')

        if validateLength(self.__rooms):
            for x in self.__rooms:

                print(f'Room number : {x}\n')
                if  self.__rooms[x].getOccupied : 

                    print('Unoccupied room.')
                else:

                    print('Occupied room\n')
                print('-------------------------')
        else:

            print('There are no rooms created.\n')


    def createRoom(self):

        habitacion = room()
        roomNumber = int(input('Enter the new room number : '))

        while validateNumber(self.__rooms,roomNumber) == False:
            roomNumber = int(input('Enter the new room number : '))

        habitacion.setRoomNumber(roomNumber)
        self.__rooms[roomNumber] = habitacion


    def addEmployee(self):

            newEmployee = employee()
            number = int(input('Enter the new employee id : '))

            while validateNumber(self.__employees,number) == False:
                number = int(input('Enter the new employee id : '))
            
            newEmployee.createEmployee(number)
            self.__employees[number] = newEmployee
    
    def showEmployees(self):



        if validateLength(len(self.__employees)):
            for x in self.__employees:
                self.__employees[x].showData()

        else:
            print('There are no employees working.\n')
    
            
    

    
 