class fun_mate:
    ''' 
     Este usará las funciones de la práctica del módulo 6
    '''

    def __init__(self):
        pass

    def es_primo(self, numero):
        primo = True
        for i in range(2,numero):
            if (numero % i==0):
                primo=False
            break
        return primo

    def repetidos(self, listarepetidos, mas_o_menos):
        repetido = listarepetidos[0]
        veces = 0
        for i in listarepetidos:
            num4 = listarepetidos.count(i)
            if (mas_o_menos == 1):
                if (listarepetidos.count(repetido) < num4):
                    repetido = i
                    veces = listarepetidos.count(i)
            else:
                if (listarepetidos.count(repetido) > num4):
                    repetido = i
                    veces= listarepetidos.count(i)
        return repetido, veces

    def conversion(self, valor, grad1, grad2):
        if (grad1 != grad2):
            if (grad1 == 'C'):
                if (grad2 == 'K'):
                    valor += 273.15
                else:
                    valor = (valor * 9 / 5) +32
            if (grad1 == 'K'):
                valor -= 273.15
                if (grad2 == 'F'):
                    valor = (valor * 9 / 5) +32
            if (grad1 == 'F'):
                valor = 5/9*(valor-32)
                if (grad2 == 'K'):
                    valor = valor + 273.15
        return valor
    
    def factorial (self, num):
        if (num >= 0):
            fact = 1
            for i in range (1,num+1):
                fact = fact * i
            return fact
        else:
            return ('No es un numero entero positivo')

val = fun_mate()