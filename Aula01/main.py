#Sem paremtros e sem retorno
def imprimirOla():
    print("Olá Pessoal")    
    print("Bem Vindos ao novo semestre") 

#Com paraemtros e com retorno
def getCalcularSalario(horas, valorHora):
    if horas == None or valorHora == None:
        return None
    else: 
         salario = horas * valorHora
         return salario   

#Com paraemtros e sem retorno
def imprimirSalario(horas, valorHora):
    salario = horas * valorHora
    print("Salario: ", salario)

#Com paraemtros e sem retorno
def imprimirSalario2(horas = 220, valorHora = 40): # podemos passar os parametros com valor default e mudar na hora de chamar metedo. isso impede que o programa não rode caso não seja passado os paramteros.
    if horas == None:
        horas = 220

    if valorHora == None:
        valorHora = 10

    salario = getCalcularSalario(horas, valorHora)
    print("Salario 2:", salario)

#Sem parametros e com retorno
def getValorPI():
    return 3.14

#Imprimir raio circulo
areaCirculo = getValorPI() * (2 * 2)
print("Area do circulo com raio 2: ", areaCirculo)

imprimirOla()

imprimirSalario(100, 30)

imprimirSalario2(100, 20)

imprimirSalario2()

imprimirSalario2(150)

imprimirSalario2(None, 60)

imprimirSalario2(100, None)

carros = ["Uno", "Doblo","Toro"]
print(carros)

print(carros[2])

posicao = int(input("Infome a posição do veiculo (de 0 a 2): "))

print("Carro Selcionado é: ", carros[posicao])


