   #PUNTO 2
def punto2():

    numero = int(input("Escriba cualquier numero para determinar si es primo: "));
    i = 1
    comprobar = 0;

    while(i < numero):
        if(numero%i == 0):
            comprobar = comprobar + 1
        i = i +1

    if comprobar <= 2:
        return print("Este numero es primo!!")
    else:
        return print("Este numero no es primo!!")
