# Função para soma
def soma(x, y):
    return x + y

# Função principal
 operador =input("Digite a operação: ")
        if operador == "soma":
            num1= int(input("digite o primeiro número: "))
            num2= int(input("digite o segundo número; "))
            result= soma(num1, num2)
            print("resultado da soma: " + str(result))
            lista_contas.append(str(num1) + " + " + str(num2) + " = "+ str(result))
