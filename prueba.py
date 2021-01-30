class prueba():

    def __init__(self):

        self.__nombre = 'Diego'


    
    @property
    def getNombre(self):
        return self.__nombre

  


diego = prueba


print(diego.getNombre)