import pickle
from employee import *
from room import *
from customer import *


class hotel():

    def __init__(self):

        self.__hotelName = ''
        self.__hotelManager = employee()
        self.__roomList = []
        try:
            roomNumbers = open('roomNumbers.txt','x')
            roomNumbers.close()
        except:
            print('File already created.\n')
         
        


    def getHotelManager(self):
        return self.__hotelManager

    def getHotelName(self):
        return self.__hotelName
    
    def setHotelName(self,name):
        self.__hotelName = name
    
    def setHotelManager(self,manager):
        self.__hotelManager = manager
    
    def deleteHotelManager(self):
        del(self.__hotelManager)


    def createHotel(self):
        self.__hotelName = input('Enter hotel name : ')
        print('\nEnter the hotel manager info')
        self.__hotelManager.createEmployee()


    def validateRoomNumber(self, number):
        if len(self.__roomList) == 0:
            return True
        else:
            for x in self.__roomList:
                if(x.getRoomNumber()) == number:
                    print('Number already in use.\n')
                    return False
            return True

        return False



    def createRoom(self):

        habitacion = room()
        roomNumber = int(input('Enter the new room number : '))

        while self.validateRoomNumber(roomNumber) == False:
            roomNumber = int(input('Enter the new room number : '))
        habitacion.setRoomNumber   = roomNumber




    

    
            
    

    
