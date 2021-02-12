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
        self.__customers = {}

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
    
    def getRooms(self):
        return self.__rooms
    
    def setRooms(self,roomss):
        self.__rooms = roomss

    
     
    def managerInfo(self):
        manager = self.getHotelManager()
        print('Manager info\n')
        manager.showData()
    

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------CUSTOMERS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def deleteGroup(self):
        if len(self.__customers) > 0:
            print('If you know the group\'s id press 1.')
            print('If you know the group\'s room number press 2.')
            
            try:
                option = int(input(': '))
            
            except:
                print('Could not delete the group.\n')
            
            if option == 1:
                try:
                    number = int(input('Enter the group id : '))
                    self.__rooms[self.__customers[number].getRoomNumber()].vacateRoom()
                    del(self.__customers[number])
                    print('Group deleted.\n')
                except:
                    print('Could not delete the group\n')
            
            elif option == 2:

                try:
                    number = int(input('Enter the group\'s room number : '))
                    
                    id = self.__rooms[number].getRoomGroup().getGroupId()
                    self.__rooms[number].vacateRoom()
                    del(self.__customers[id])
        
                    print('Group deleted.\n')
                
                except:
                    print('Could not delete the group\n')
            
            else:
                print('Invalid option.\n')
        else:
            print('There are no customers in the hotel')                





  
    
    
    def showCustomersGroups(self):
        if len(self.__customers) > 0:
            print('\n\n\nCUSTOMERS LIST :')
            for i in self.__customers:
                print('\n\n------------------------------------------')
                print(f'\nGroup id : {self.__customers[i].getGroupId()}')
                print(f'Days of stay : {self.__customers[i].getGroupRepresentative().getDays()}')
                print(f'Group representative name : {self.__customers[i].getGroupRepresentative().getName()}')
                print(f'Group\'s room number : {self.__customers[i].getRoomNumber()}\n')
                print('------------------------------------------\n')
        else:
            print('There are no customers in the hotel.\n')

    def addCustomer(self):

        
        
        group = customerGroup()

        if len(self.__rooms) > 0 and len(self.__customers) < len(self.__rooms):

            id = int(input('\nEnter the group id : '))

            while validateNumber(self.__customers,id) == False:
                id = int(input('Enter the group id : '))

            group.createGroup(id)

            if self.fillRoom(group) == False:
                print('Try to add the customers again.\n')
            

        else:

            print('There are no free rooms to locate the customers.\n')



#---------------------------------------------------------ROOM-------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fillRoom(self,customers):

        self.showFreeRooms()
        number = 0

        while(self.validateRoomNumber(number) == False):
            try:
                number = int(input('\nEnter the room number that you want : '))

            except:
                print('Invalid number.\n')
                return False

        if self.__rooms[number].getOccupied() == False:
            customers.setRoomNumber(number)
            self.__rooms[number].setRoomGroup(customers)
            self.__rooms[number].setOccupied(True)
            self.__customers[customers.getGroupId()] = customers
            print('Customers added to the hotel.\n')
            return True

        elif self.__rooms[number].getOccupied() == False:
            print('Room being occupied.\n')

        else:

            print('Could not ad customers.\n')
            return False


    def validateRoomNumber(self,number):
        
        lista = self.__rooms.values()
        for i in lista:
            
            if(i.getRoomNumber() == number):
                return True


        return False

    def showFreeRooms(self):

        lista = self.__rooms.values()
        cont = 0
        print('\n\n')
        for i in lista:

            if i.getOccupied() == False:
                
                print(f'\nRoom number : {i.getRoomNumber()}')
                print('------------------------------\n')
                cont+= 1
        print(f'\nTotal free rooms : {cont}\n')


    
    def showRooms(self):

        if validateLength(len(self.__rooms)):
            
            for x in self.__rooms:
                print('-------------------------')
                print(f'Room number : {x}\n')
                if  self.__rooms[x].getOccupied() == False: 

                    print('Unoccupied room.')
                else:

                    print('Occupied room\n')
                print('-------------------------')
            print(f'Total number of rooms : {len(self.__rooms)}\n')
        else:

            print('There are no rooms created.\n')


    def createRoom(self):

        habitacion = room()
        roomNumber = int(input('Enter the new room number : '))

        while validateNumber(self.__rooms,roomNumber) == False:
            try:
                roomNumber = int(input('Enter the new room number : '))
            except:
                print('Only numbers accepted.\n')

        habitacion.setRoomNumber(roomNumber)
        self.__rooms[roomNumber] = habitacion

    def removeRoom(self,roomNumber):
        try:
            if self.__rooms[roomNumber].getOccupied() == True:

                print('Room is being used, delete it when free.\n')
                return None   
            else:

                del(self.__rooms[roomNumber])
        except:
            print('Could not remove the room.\n')


    def deleteRoom(self):
        if len(self.__rooms) > len(self.__customers):

            roomNumber = int(input('Enter the room\'s number that you wanna delete : '))
            self.removeRoom(roomNumber)
        else:
            print('There are no free rooms to delete.\n')


#--------------------------------------------------EMPLOYEE------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def changeEmployeeData(self):

        if len(self.__employees) > 0:
            salary = 0
            position = ''
            name = ''
            nation = ''
            age = 0
            self.showEmployees()
            id = int(input('Enter the employee\'s id : '))
            while True:

                print('Select 1 to change the employee\'s salary')   
                print('2 ro change the employee\'s position') 
                print('3 to change the employee\'s name')
                print('4 to change the employee\'s nationality')
                print('5 to change the employee\'s age')
                option = int(input('\n:'))

                if option == 1:
                    salary = int(input('Enter the new salary : '))

                elif option == 2:
                    position = input('ENter the new position : ')

                elif option == 3:
                    name = input('Enter the new name : ')

                elif option == 4:
                    nation = input('Enter the new nationality : ')
                    
                elif option == 5:
                    age = int(input('Enter the new age : '))

                else:

                    print('Invalid ID.\n')
                
                print('\nSelect 1 to save changes.')
                print('Select 2 to keep changing')
                print('Select 3 to cancel the changes.')
                option = int(input(':'))

                if option == 1:
                    self.__employees[id].modifyEmployee(position,salary,name,nation,age)
                    break
                elif option == 3:
                    break
        
        else:
            print('There are no employees in the hotel.\n')
        


    def addEmployee(self):

            print('\nENTER THE EMPLOYEE DATA.\n')
            newEmployee = employee()
            number = int(input('Enter the new employee id : '))

            while validateNumber(self.__employees,number) == False:
                try:
                    number = int(input('Enter the new employee id : '))
                except:
                    print('Enter a number.')
                    return None
            
            newEmployee.createEmployee(number)
            self.__employees[number] = newEmployee
    


    def showEmployees(self):

        if validateLength(len(self.__employees)):
            for x in self.__employees:
                self.__employees[x].showData()

        else:
            print('There are no employees working.\n')
    
            
    
    def deleteEmployee(self):
        
        if len(self.__employees) > 0:
            print('Do you know the employee\'s id?\n1 Yes\n2 No')
            option = int(input('Enter your option : '))

            if option == 2:

                
                self.showEmployees()
                
                id = int(input('\nChose the employee\'s id : '))
                self.eraseEmployee(id)

            elif option == 1:
                id = int(input('Enter the id of the employee that you want to delete : '))
                self.eraseEmployee(id)

            else:
                print('Invalid option.\n')
        else:
            print('There are no employees in the hotel.\n')

    def eraseEmployee(self,id):
        try:
            del(self.__employees[id])
        except:
            print('Could not remove employee.\n')
    

    
 