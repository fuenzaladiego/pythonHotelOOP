from person import human

class customer(human):

    def __init__(self):
        self.__daysOfStay = 0
        self.__roomNumber = 0

    
    def createCustomer(self,days):
        super().createHuman()
        self.__daysOfStay = days

    def showData(self):
        super().showData()
        print(f'Days of stay : {self.__daysOfStay}\n--------------------------\n')
    
        

class customerGroup():

    def __init__(self):
        self.__groupRepresentative = 'None'
        self.__groupList = []

    @property
    def getRepresentative(self):
        print('\n-------------GROUP REPRESENTATIVE DATA-------------')
        return self.__groupRepresentative

    def createGroup(self):

        groupSize = 0
        while groupSize <= 0:
            groupSize = int(input('Enter the group size : '))

        daysOfStay = 0
        while daysOfStay <= 0:
            daysOfStay = int(input('Enter days of stay : '))

        for x in range(groupSize):
            customerAux = customer()
            customerAux.createCustomer(daysOfStay)
            self.__groupList.append(customerAux)

        print('\n')
        print('Select the group representatice\n')
        self.setRepresentative()


    def groupListing(self):

        if len(self.__groupList) > 0:
            print(self.__groupRepresentative)
            for x in self.__groupList:
                x.showData()
        else:
            print('No customers in the group')

    def setRepresentative(self):

        if len(self.__groupList) == 1:
            self.__groupRepresentative = self.__groupList[0]

        else:
            if len(self.__groupList) > 0:
                self.groupListing()
                while  self.__groupRepresentative == 'None' :

                    representativeAux = input('Enter the name of the group representative : ')
                    for x in self.__groupList:
                        if representativeAux.lower() == x.getName.lower():
                            self.__groupRepresentative = x
                            break
                        
                    



