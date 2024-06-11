# Calculadora?

while True:
    print("\n\t\t\t -- Calculadora Simples --")

    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    op = int(input("\nOpção: "))

    if op == 1:
        print("\n\t\t\t -- Soma -- \n")

        #Entrada de dados
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        #Processamento dos dados
        total = n1 + n2

        #Saída dos dados
        print("\n\t\t {} + {} = {:.2f}\n".format(n1, n2, total))
    
    if op == 2:
        print("\n\t\t\t -- Subtração -- \n")

    #Entrada de dados
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        #Processamento dos dados
        total = n1 - n2

        #Saída dos dados
        print("\n\t\t {} - {} = {:.2f}\n".format(n1, n2, total))
    
    if op == 3:
        print("\n\t\t\t -- Multiplicação -- \n")
    #Entrada de dados
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        #Processamento dos dados
        total = n1 * n2

        #Saída dos dados
        print("\n\t\t {} * {} = {:.2f}\n".format(n1, n2, total))
    
    if op == 4:
        print("\n\t\t\t -- Divisão -- \n")

        #Entrada de dados
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        #Processamento dos dados
        total = n1 / n2

        #Saída dos dados
        print("\n\t\t {} / {} = {:.2f}\n".format(n1, n2, total))

    elif op == 5:
        print("\n\nFinal da execução\n\n")
        break
    else:
        if op >= 6:
            print("\n\nOpção {} incorreta.\n\n".format(op))