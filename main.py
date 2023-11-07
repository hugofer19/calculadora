operador = input("Qual operação deseja? (+, -, *, /): ")
num1 = float(input("Coloca o número 1: "))
num2 = float(input("Coloca o número 2: "))
resultado = 0

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        exit()
else:
    print("Operador inválido. Use apenas '+', '-', '*', '/'.")

print("O resultado é: " + str(resultado))
