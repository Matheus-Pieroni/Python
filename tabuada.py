
#Calculo da tabuada!

print("\n\t\t\t -- Tabuada Universal -- \n")

while True:
    print("\n\t\t\t 1. Iniciar a tabuada \n")
    print("\n\t\t\t 2. Sair \n")
    op = int(input("\nOpção: "))

    if op == 1:
        #input
        nume = int(input("\n Qual número? \n"))
        repet = int(input("\n Quantas vezes? \n"))

        #output em print
        while repet >= 0:
            total = nume * repet
            print("\n\t\t {} * {} = {} \n".format(nume,repet,total))
            repet = repet - 1
    
    elif op == 2:
        print("\n\nFinal da execução\n\n")
        break
    else:
        if op >= 3:
            print("\n\nOpção {} incorreta.\n\n".format(op))