from customer import *


class room():

    def __init__(self):

        self.__roomNumber = 0
        self.__roomGroup = customerGroup()
        self.__occupied = False

    def createRoom(self):

        self.__roomNumber = int(input('Enter the room number : '))


    def occupyRoom(self):

        self.__roomGroup.createGroup()
        self.__occupied = True    

    @setRoomNumber.setter
    def setRoomNumber(self,number):
        self.__roomNumber = number
    @setRoomGroup.setter
    def setRoomGroup(self, group):
        self.__roomGroup = group
    @setOccupied.setter
    def setOccupied(self,state):
        self.__occupied = state
    @property
    def getRoomNumber(self):
        return self.__roomNumber
    @property
    def getRoomGroup(self):
        return self.__roomGroup
    @property
    def getOccupied(self):
        return self.__occupied