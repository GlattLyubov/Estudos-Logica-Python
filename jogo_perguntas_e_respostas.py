print("""\n...Escolha um dos seres vivos abaixo...\n
1- Leão
2- Cavalo
3- Homem
4- Macaco
5- Morcego
6- Baleia
7- Avestruz
8- Pinguim
9- Pato 
10- Águia
11- Tartaruga
12- Crocodilo
13- Cobra-Cega
0- Sair\n""")

while True:
    escolha = int(input("Digite o número correspondente ao ser vivo escolhido: "))

    if escolha == 0:
        print("Saindo do programa. Até mais!")
        break

    elif escolha == 1:
        print("Leão")
        print("Você escolheu Leão, guarde essa escolha na memória!")
        break
    
    elif escolha == 2:
        print("Cavalo")
        print("Você escolheu Cavalo, guarde essa escolha na memória!")
        break

    elif escolha == 3:
        print("Homem")
        print("Você escolheu Homem, guarde essa escolha na memória!")
        break

    elif escolha == 4:
        print("Macaco")
        print("Você escolheu Macaco, guarde essa escolha na memória!")
        break

    elif escolha == 5:
        print("Morcego")
        print("Você escolheu Morcego, guarde essa escolha na memória!")
        break

    elif escolha == 6:
        print("Baleia")
        print("Você escolheu Baleia, guarde essa escolha na memória!")
        break

    elif escolha == 7:
        print("Avestruz")
        print("Você escolheu Avestruz, guarde essa escolha na memória!")
        break

    elif escolha == 8:  
        print("Pinguim")
        print("Você escolheu Pinguim, guarde essa escolha na memória!")
        break

    elif escolha == 9:
        print("Pato")
        print("Você escolheu Pato, guarde essa escolha na memória!")
        break

    elif escolha == 10:
        print("Águia")
        print("Você escolheu Águia, guarde essa escolha na memória!")
        break

    elif escolha == 11:
        print("Tartaruga")
        print("Você escolheu Tartaruga, guarde essa escolha na memória!")
        break

    elif escolha == 12:
        print("Crocodilo")
        print("Você escolheu Crocodilo, guarde essa escolha na memória!")
        break

    elif escolha == 13:
        print("Cobra-Cega")
        print("Você escolheu Cobra-Cega, guarde essa escolha na memória!")
        break
    
    else:
        print("Opção inválida. Por favor, escolha um número entre 0 e 13.")

print("\n...Você escolheu um ser vivo, agora vou tentar adivinhar qual foi com perguntas de sim ou não...\n")

while True:

    resposta = input("O ser vivo que você escolheu é um mamífero? (S/N): ").upper()

    if resposta == 'S':
        print("Ele é Quadrúpede?")
        resposta = input("Sim ou Não? (S/N): ").upper()

        if resposta == 'S':
            print("Ele é Carnívoro?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'S':
                print("O ser vivo que você escolheu é o Leão!")
                break
                

            elif resposta == 'N':
                print("Ele é um Herbívoro?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é o Cavalo!")
                    break

        elif  resposta == 'N':
            print("Ele é Bípede?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'S':
                print("Ele é Onívoro?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é o Homem!")
                    break
                    
                
                if resposta =='N':
                    print("Ele é Frutívero?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Macaco!")
                        break
                        

            elif resposta == 'N':
                print("Ele é voador?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é o Morcego!")
                    break

                elif resposta == 'N':
                    print("Ele é Aquático?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é a Baleia!")
                        break

    elif resposta == 'N':
        print("\nEntão o ser vivo que você escolheu não é um mamífero.")
        print("...Vamos continuar com as perguntas, preste bem atenção...\n")
        print("Ele é uma ave?")
        resposta = input("Sim ou Não? (S/N): ").upper() 

        if resposta == 'S':
            print("Ele sabe voar?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'N':
                print("Ele é maior que um ser humano?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S': 
                    print("O ser vivo que você escolheu é o Avestruz!")
                    break

                elif resposta == 'N':
                    print("Ele vive em regiões muito frias?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Pinguim!")
                        break

            elif resposta == 'S':
                print("Ele sabe nadar?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é o Pato!")
                    break

                elif resposta == 'N':
                    print("Ele é um animal de rapina?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é a Águia!")
                        break
        
        elif resposta == 'N':
            print("\nBom, então não é um mamífero e nem uma ave...\n")
            print("É um réptil?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'S':
                print("Ele tem casco?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é a Tartaruga!")
                    break

                elif resposta == 'N':
                    print("Ele é Carnívoro?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Crocodilo!")
                        break

                    elif resposta == 'N':
                        print("\nVamos usar a lógica para descobrir qual é o ser vivo que você escolheu...")
                        print("Se ele não é um mamífero, nem uma ave, mas é um réptil, não tem casco e não é carnívoro...\n")
                        print("Então só pode ser a Cobra-Cega! Lembrando que a cobra-cega é um anfíbio que não possui patas, tem pele úmida e vive enterrada.")
                    
                    break
