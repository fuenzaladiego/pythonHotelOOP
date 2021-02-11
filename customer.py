from person import human

class customer(human):

    def __init__(self):
        self.__daysOfStay = 0


    
    def createCustomer(self,days):
        super().createHuman()
        self.__daysOfStay = days
        print('\n')

    def showData(self):
        super().showData()
        print(f'Days of stay : {self.__daysOfStay}\nRoom number : {self.__roomNumber}\n--------------------------\n')

    

    def getDays(self):
        return self.__daysOfStay

    

    def setDays(self,days):
        self.__daysOfStay = days

       

    def deleteDays(self):
        
        self.__daysOfStay = None
        
    def deleteRoomNumber(self):
        self.__roomNumber = None
        

class customerGroup():

    def __init__(self):
        self.__groupList = []
        self.__groupRepresentative = human()
        self.__groupId = 0
        self.__roomNumber = -1
    
    def getGroupList(self):
        return self.__groupList

    def getGroupId(self):
        return self.__groupId

    def setGroupId(self,id):
        self.__groupId = id


    def getGroupRepresentative(self):
        return self.__groupRepresentative

    def setGroupRepresentative(self, representative):
        self.__groupRepresentative = representative

    def representativeData(self):
        self.getGroupRepresentative().showData

    def setRoomNumber(self, number):
        self.__roomNumber = number
        
    def getRoomNumber(self):
        return self.__roomNumber

    def createGroup(self, id):

        groupSize = 0
        while groupSize <= 0:
            groupSize = int(input('\nEnter the group size : '))

        daysOfStay = 0
        while daysOfStay <= 0:
            daysOfStay = int(input('Enter days of stay : '))
        self.__groupId = id

        for x in range(groupSize):
            print('\nENTER THE CUSTOMER DATA.\n')
            customerAux = customer()
            customerAux.createCustomer(daysOfStay)
            self.__groupList.append(customerAux)

        print('\n')
        if len(self.__groupList) > 1:
            print('\nSELECT THE GROUP REPRESENTATIVE\n')
        self.selectGroupRepresentative()
            
        
    def groupListing(self):

        if len(self.__groupList) > 0:
            for x in self.__groupList:
                x.showData()
        else:
            print('\nNo customers in the group\n')

    
    def selectGroupRepresentative(self):
        
        control = True

        if len(self.__groupList) == 1:
            self.__groupRepresentative = self.__groupList[0]

        else:
            
            while control:
                representativeName = input('Enter the group representative name : ')
                representativeAge = int(input('Enter the group representative age : '))
                for x in self.__groupList:
                    

                    if x.getName() == representativeName and x.getAge() == representativeAge:
                        self.setGroupRepresentative(x)
                        control = False
                        break
                



                    



