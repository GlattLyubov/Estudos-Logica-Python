
# Jogo de Perguntas e Respostas em Python
# Desenvolvido por: Matheus Cabral

print('''
    Bem-vindo ao jogo de perguntas e respostas!
    
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
0- Sair
      
Escolha um número de 1 a 13 para escolher um animal, ou 0 para sair do jogo.      
''')

while True:
    escolha = int(input("Digite o número correspondente ao ser vivo escolhido: "))

    if escolha == 0:
        print("Saindo do programa. Até mais!")
        break

    elif escolha == 1:
        print("Leão")
        print("Você escolheu Leão, guarde essa escolha na memória!")
        
    elif escolha == 2:
        print("Cavalo")
        print("Você escolheu Cavalo, guarde essa escolha na memória!")
        
    elif escolha == 3:
        print("Homem")
        print("Você escolheu Homem, guarde essa escolha na memória!")
        
    elif escolha == 4:
        print("Macaco")
        print("Você escolheu Macaco, guarde essa escolha na memória!")
        
    elif escolha == 5:
        print("Morcego")
        print("Você escolheu Morcego, guarde essa escolha na memória!")
        
    elif escolha == 6:
        print("Baleia")
        print("Você escolheu Baleia, guarde essa escolha na memória!")
        
    elif escolha == 7:
        print("Avestruz")
        print("Você escolheu Avestruz, guarde essa escolha na memória!")
        
    elif escolha == 8:  
        print("Pinguim")
        print("Você escolheu Pinguim, guarde essa escolha na memória!")
        
    elif escolha == 9:
        print("Pato")
        print("Você escolheu Pato, guarde essa escolha na memória!")
        
    elif escolha == 10:
        print("Águia")
        print("Você escolheu Águia, guarde essa escolha na memória!")
        
    elif escolha == 11:
        print("Tartaruga")
        print("Você escolheu Tartaruga, guarde essa escolha na memória!")
        
    elif escolha == 12:
        print("Crocodilo")
        print("Você escolheu Crocodilo, guarde essa escolha na memória!")
        
    elif escolha == 13:
        print("Cobra-Cega")
        print("Você escolheu Cobra-Cega, guarde essa escolha na memória!")
        

    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 13 ou 0 para sair.")


    while escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5 or escolha == 6 or escolha == 7 or escolha == 8 or escolha == 9 or escolha == 10 or escolha == 11 or escolha == 12 or escolha == 13:

        resposta = input("\nO ser vivo que você escolheu é um mamífero? (S/N): ").upper()
        
        if resposta == "S":
            print("\nEle é Quadrúpede?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'S':
                print("\nEle é Carnívoro?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("O ser vivo que você escolheu é o Leão!\n")
                    break
                

                elif resposta == 'N':
                    print("\nEle é um Herbívoro?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Cavalo!\n")
                        break

            elif resposta == 'N':    
                print("\nEle é Bípede?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("\nEle é Onívoro?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Homem!\n")
                        break

                    elif resposta == 'N':
                        print("Ele é Frutívoro?")
                        resposta = input("Sim ou Não? (S/N): ").upper()

                        if resposta == 'S':
                            print("O ser vivo que você escolheu é o Macaco!\n")
                            break

                elif resposta == 'N':
                    print("\nEle é voador?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Morcego!\n")
                        break

                    elif resposta == 'N':
                        print("\nEle é Aquático?")
                        resposta = input("Sim ou Não? (S/N): ").upper()

                        if resposta == 'S':
                            print("O ser vivo que você escolheu é a Baleia!\n")
                            break       

        elif resposta == "N":
            print("\nEntão o ser vivo que você escolheu não é um mamífero.")
            print("...Vamos continuar com as perguntas, preste bem atenção...\n")
            print("Ele é uma ave?")
            resposta = input("Sim ou Não? (S/N): ").upper()

            if resposta == 'S':
                print("\nEle sabe voar?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'N':
                    print("\nEle é maior que um ser humano?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Avestruz!\n")
                        break

                    elif resposta == 'N':
                        print("\nEle vive em regiões polares?")
                        resposta = input("Sim ou Não? (S/N): ").upper()

                        if resposta == 'S':
                            print("O ser vivo que você escolheu é o Pingüim!\n")
                            break

                elif resposta == 'S':
                    print("\nEle sabe nadar?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Pato!\n")
                        break

                    elif resposta == 'N':
                        print("\nEle é um animal de rapina?")
                        resposta = input("Sim ou Não? (S/N): ").upper()

                        if resposta == 'S':
                            print("O ser vivo que você escolheu é a Águia!\n")
                            break
            
            elif resposta == 'N':
                print("\nBom, então não é um mamífero e nem uma ave...")
                print("É um réptil?")
                resposta = input("Sim ou Não? (S/N): ").upper()

                if resposta == 'S':
                    print("\nEle tem casco?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é a Tartaruga!\n")
                        break

                elif resposta == 'N':
                    print("\nEle é Carnívoro?")
                    resposta = input("Sim ou Não? (S/N): ").upper()

                    if resposta == 'S':
                        print("O ser vivo que você escolheu é o Crocodilo!\n")
                        break

                    elif resposta == 'N':
                        print("\nVamos usar a lógica para descobrir qual é o ser vivo que você escolheu...")
                        print("Se ele não é um mamífero, nem uma ave, mas é um réptil, não tem casco e não é carnívoro...")
                        print("Então só pode ser a Cobra-Cega! Lembrando que a cobra-cega é um anfíbio que não possui patas, tem pele úmida e vive enterrada.\n")
                        break
            
        else:
            print("\nResposta inválida. Por favor, responda com 'S' para sim ou 'N' para não.\n")