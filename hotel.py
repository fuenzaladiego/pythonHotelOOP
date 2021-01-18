import pickle
from employee import *

class hotel():

    def __init__(self):

        self.__hotelName = ''
        self.__hotelManager = employee()
        self.__hotelManager.createEmployee()
        self.__roomList = []
        try:
            roomNumbers = open('roomNumbers.txt','x')
        except:
            print('File already created.\n')
        finally:
            roomNumbers.close()
        

    @property
    def getHotelManager(self):
        return self.__hotelManager
    @property
    def getHotelName(self):
        return self.__hotelName

    def validateRoomNumber(self, number):
        fileh = open('roomNumbers.txt','r')
        text = ''
        for x in fileh:
            text+= str(x)

        array = text.split(' ')
        fileh.close()

        for x in array:
            if number == int(array):
                print('Room number already in use.\n')
                return False

        print('Valid room number\n')
        return True


    def createRoom(self):
        control = True
        archivo = open('roomNumbers.txt','w')
        while(control):
            roomNumber = int(input('Enter the new room number: '))
            if self.validateRoomNumber(roomNumber):
                archivo.write(str(roomNumber)+' ')
                control = False

    
            
    

    
