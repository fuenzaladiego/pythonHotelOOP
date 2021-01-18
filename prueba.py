

archivo = open('prueba.txt','r')
string = ''
numero = 3
for x in archivo:
    string+= str(x)

array = string.split(' ')
print(array)
for x in array:
    print(x)
    if int(x) == numero:
        print('Eureka!!')
        break