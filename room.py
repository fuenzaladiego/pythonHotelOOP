from customer import *


class room():

    def __init__(self):

        self.__roomNumber = int
        self.__roomGroup = customerGroup()
        self.__occupied = False


    def occupyRoom(self, group):
 
        self.__roomGroup.setRoomGroup(group)
        self.setOccupied(True)  

    def vacateRoom(self):
        del(self.__roomGroup)
        self.setOccupied(False)




    def setRoomNumber(self,number):
        self.__roomNumber = number

    def setRoomGroup(self, group):
        self.__roomGroup = group

    def setOccupied(self,state):
        self.__occupied = state

    def getRoomNumber(self):
        return self.__roomNumber

    def getRoomGroup(self):
        return self.__roomGroup

    def getOccupied(self):
        return self.__occupied
    
