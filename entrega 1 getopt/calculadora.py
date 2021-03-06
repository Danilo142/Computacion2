import sys
import getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')


for (op, ar) in opt:
    if op in '-o':
        operador = ar
    elif op == '-n':
        num1 = ar
    elif op == '-m':
        num2 = ar
    else:
        print("Opcion Invalida")

if operador == '+':
    print("El resultado de la suma de:", num1, "+", num2, "es:", int(num1) + int(num2))
elif operador == '-':
    print("El resultado de la resta de:", num1, "-", num2, "es:", int(num1) - int(num2))
elif operador == '*':
    print("El resultado de la multiplicacion de:", num1, "*", num2, "es:", int(num1) * int(num2))
elif operador == '/':
    print("El resultado de la division de:", num1, "/", num2, "es:", int(num1) / int(num2))
else:
    print("Ingrese una opcion valida")