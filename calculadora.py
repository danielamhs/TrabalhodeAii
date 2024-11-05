# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao (x, y):
    return x / y
    
# Função principal
def calculadora():
    lista_contas=[]
    while True:
        operador =input("Digite a operação: ")
        if operador == "soma":
            num1= int(input("digite o primeiro número: "))
            num2= int(input("digite o segundo número; "))
            result= soma(num1, num2)
            print("resultado da soma: " + str(result))
            lista_contas.append(str(num1) + " + " + str(num2) + " = "+ str(result))
                elif operador == "sub":
            num1= int(input("digite o  primeiro número: "))
            num2= int(input("digite o segundo número"))
            result= subtracao(num1, num2)
            print("resultado da subtração: " + str(result))
            lista_contas.append(str(num1) + " - " + str(num2) + "=" + str(result))
        elif operador == "mult":
            num1= int(input("digite o primeiro número: "))
            num2= int(input("digite o segundo número: "))
            result= multiplicacao(num1, num2)
            print("resultado da multiplicação: " + str(result))
            lista_contas.append(str(num1) + "*" + str(num2) + "=" + str(result))
        elif operador == "div":
            num1= int(input("digite o primeiro número: "))
            num2= int(input("digite o segundo ´número: "))
            result= divisao(num1, num2)
            print("resultado da divisão: " + str(result))
            lista_contas.append(str(num1) + "/" + str(num2) + "=" + str(result))
        elif operador == ("hist"):
            if len(lista_contas) == 0:
                print("sem nenhuma operação")
            for item in lista_contas:
                print(item)
        else:
            print("operacao nao suportada")
        print(lista_contas)

# Excutar a calculadora
calculadora()
