from hotel import * 


class menuI():

    def __init__(self):
        self.__miHotel = hotel()
        self.option = 0
    
    def deployMenu(self):
        while(True):
            print(f'                 {self.__miHotel.getHotelName().upper()}')
            print('------------------------------------------\n')
            print('Press 1 to create a room.')
            print('Press 2 to add a employee.')
            print('Press 3 to add a customer group to the hotel.')
            print('Press 4 to delete a room.')
            print('Press 5 to delete an employee.')
            print('Press 6 to delete a customer group.')
            print('Press 7 to see a list of the hotel employees.')
            print('Press 8 to see a list of the hotel rooms.')
            print('Pres 9 to see a list of the unoccupied hotel rooms.')
            print('Press 10 to see a list of the customer groups')
            print('Press 11 to modify an employee.')
            print('Press 12 to see the manager info.')
            print('Press 13 to close the console.')
            print('\n------------------------------------------')
            try:
                option = int(input(': '))
                if self.validateOption(option) == False:
                    print('Invalid option.\n')

                else:
                    if option == 13:
                        break
                    
                    else:
                        self.useOption(option)
                        

            except:
                print('Invalid option.\n')

        print('Thank you for using me.\n')


    def useOption(self,number):

        if number == 1:
            self.__miHotel.createRoom()

        elif number == 2:
            self.__miHotel.addEmployee()

        elif number == 3:
            self.__miHotel.addCustomer()

        elif number == 4:
            self.__miHotel.deleteRoom()

        elif number == 5:
            self.__miHotel.deleteEmployee()

        elif number == 6:
            self.__miHotel.deleteGroup()

        elif number == 7:
            self.__miHotel.showEmployees()

        elif number == 8:
            self.__miHotel.showRooms()

        elif number == 9:
            self.__miHotel.showFreeRooms()

        elif number == 10:
            self.__miHotel.showCustomersGroups()

        elif number == 11:
            self.__miHotel.changeEmployeeData()

        elif number == 12:
            self.__miHotel.__employees[1].showData()





    def validateOption(self,number):


        if number < 1:
            return False
        elif number > 13:
            return False
        else:
            return True

