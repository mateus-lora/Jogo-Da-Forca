#ALUNO:Mateus Lora  RA:1136218
import os, time

def limpar_tela():
    os.system("cls")

def aguarde(segundos):
    time.sleep(segundos)

def iniciar_jogo():
    limpar_tela()
    os.system("color F")
    print("ATENÇÃO! Para uma melhor experiência PRESS ^ (Full Screen)")
    aguarde(4)
    input("PRESS enter to continue...")
    limpar_tela()
    os.system("color E")
    print('''  
        ██╗ ██████╗ █████╗  ██████╗    ██████╗  █████╗     ███████╗ ██████╗██████╗  ██████╗ █████╗          
        ██║██╔══██╗██╔═══╝ ██╔══██╗    ██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗   
        ██║██║  ██║██║ ███╗██║  ██║    ██║  ██║███████║    ███████╗██║  ██║██████╔╝██║     ███████║  
   ██   ██║██║  ██║██║  ██║██║  ██║    ██║  ██║██╔══██║    ██╔════╝██║  ██║██╔══██╗██╝     ██╔══██║   
   ╚█████╔╝╚█████╔╝╚█████╔╝╚█████╔╝    ██████╔╝██║  ██║    ██║     ╚█████╔╝██║  ██║╚██████╗██║  ██║  
    ╚════╝  ╚════╝  ╚════╝  ╚════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝''')
    aguarde(3.5)
    limpar_tela()

    #Solicitar o nome do desafiante e do competidor ao abrir o programa;
    os.system("color F")
    print("Sejam bem-vindos! Para iniciar insiram seus nomes de usuário:")
    aguarde(1.5)
    desafiante = input("Desafiante: ")
    competidor = input("Competidor: ")
    limpar_tela()

    #Solicitar a palavra chave e as dicas para o desafiante;
    palavra_chave = input(f"{desafiante}, insira a palavra-chave para o(a) {competidor} adivinhar: ").lower()
    limpar_tela()
    dicas = []
    print(f"Para facilitar para o(a) {competidor}, insira 3 dicas:")
    aguarde(1.5)
    dicas.append (input("Dica 1: "))
    dicas.append (input("Dica 2: "))
    dicas.append (input("Dica 3: "))
    limpar_tela()

    return palavra_chave, dicas, competidor, desafiante

def jogo_da_forca(palavra_chave, dicas, competidor, desafiante):

    #Apresentar o número de letras ao competidor;
    palavra_oculta = ["*" for _ in palavra_chave]
    print(f"{competidor} a palavra-chave apresenta {len(palavra_chave)} letras:"," ".join(palavra_oculta))
    aguarde(4)
    limpar_tela()

    print("Boa sorte!")
    aguarde(2.5)
    limpar_tela()

    letras_usadas = []
    numero_de_tentantivas = 6
    erros = (0)
    

    while True:
        os.system("color F")
        limpar_tela()
        print(f"{competidor}, você tem {numero_de_tentantivas} tentativas restantes.")
        print("Palavra:", " ".join(palavra_oculta))
        print("Letras já usadas:", ", ".join(letras_usadas))
        print(f"Você errou {erros} vezes!")

        if erros == 0 :
            os.system("color 7")
            print(''' 
            +---+
            |   |
                |
                |
                |
                |
         ========
            ''')
        
        elif erros == 1 :
            os.system("color 2")
            print(''' 
            +---+
            |   |
            O   |
                |
                |
                |
         ========
            ''')
            
        elif erros == 2 :
            os.system("color 3")
            print(''' 
            +---+
            |   |
            O   |
            |   |
                |
                |
         ========
            ''')  
            
        elif erros == 3 :
            os.system("color 1")
            print(''' 
            +---+
            |   |
            O   |
           /|   |
                |
                |
         ========
            ''')
            
        elif erros == 4 :
            os.system("color 6")
            print(''' 
            +---+
            |   |
            O   |
           /|\  |
                |
                |
         ========
            ''')
            
        elif erros == 5 :
            os.system("color 5")
            print(''' 
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
         ========
            ''')
        
    
        if len(dicas) > 0 :
            #Opções jogar ou solicitar dica;
            opcao = input("PRESS a opção que você deseja? JOGAR(1) ou solicitar DICA(2) ")
            if opcao == "2": 
                print("A dica é:", dicas.pop(0))
    
                print(f"Restam {len(dicas)} dicas!")
        tentativa = input("Insira uma letra ou a palavra-chave: ").lower()
        limpar_tela()
        
        if tentativa in letras_usadas:
            print("Você já inseriu essa letra, tente outra.")
            aguarde(2.2)
            limpar_tela()
            continue
        
        letras_usadas.append(tentativa)

        if tentativa in palavra_chave:
            for i, letra in enumerate(palavra_chave):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
        
        else :           
            print("A letra que você inseriu é incorreta.")
            aguarde(2.2)
            limpar_tela()
            numero_de_tentantivas -= 1
            erros = erros + 1
            print(f"Você errou {erros} vezes!")

        if "*" not in palavra_oculta or tentativa == palavra_chave:
            os.system("color 6")
            print(f"Parabéns {competidor}, você venceu! A palavra-chave era {palavra_chave}.")
            print('''
             ##########################          
             ##########################                       
             ##########################         
      ########################################    
    ####     ##########################      ####    
     ####     ########################      ####    
      ####     ######################     ####    
        ####    ####################    ####      
          ################################        
              ########################            
                   ##############                  
                    ############                                                                                                                                     
                  ################                
                  ################                
                ####################   
''')
            aguarde(6)
            limpar_tela()
            os.system("color 4")
            print(f"Não foi dessa vez {desafiante}, você perdeu!")
            print(''' 
                                    
                        ______
                     .-"      "-.
                    /            \\     
        _          |              |          _
       ( \         |,  .-.  .-.  ,|         / )
        > "=._     | )(__/  \__)( |     _.=" <
       (_/"=._"=._ |/     /\     \| _.="_.="\_)
              "=._ (_     ^^     _)"_.="
                  "=\__|IIIIII|__/="
                 _.="| \IIIIII/ |"=._
       _     _.="_.="\          /"=._"=._     _
      ( \_.="_.="     `--------´     "=._"=._/ )
       > _.="                            "=._ <
      (_/                                    \_)
        
            
            ''')
            aguarde(6)
            limpar_tela()


        if numero_de_tentantivas == 0:
            os.system("color 4")
            print(f"{competidor} você foi ENFORCADO(a)!")
            print(''' 
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
         ========
            ''')
            aguarde(6)
            limpar_tela
           
            print(f"Não foi dessa vez {competidor}, você perdeu! A palavra-chave era {palavra_chave}.")
            print(''' 
                                    
                        ______
                     .-"      "-.
                    /            \\     
        _          |              |          _
       ( \         |,  .-.  .-.  ,|         / )
        > "=._     | )(__/  \__)( |     _.=" <
       (_/"=._"=._ |/     /\     \| _.="_.="\_)
              "=._ (_     ^^     _)"_.="
                  "=\__|IIIIII|__/="
                 _.="| \IIIIII/ |"=._
       _     _.="_.="\          /"=._"=._     _
      ( \_.="_.="     `--------´     "=._"=._/ )
       > _.="                            "=._ <
      (_/                                    \_)
        
            
            ''')
            aguarde(6)
            limpar_tela()
            os.system("color 6")
            print(f"Parabéns {desafiante}, você venceu!")
            print('''
             ##########################          
             ##########################                       
             ##########################         
      ########################################    
    ####     ##########################      ####    
     ####     ########################      ####    
      ####     ######################     ####    
        ####    ####################    ####      
          ################################        
              ########################            
                   ##############                  
                    ############                                                                                                                                     
                  ################                
                  ################                
                ####################   
''')
            aguarde(6)
            limpar_tela()
        
        #Menu oferecendo aos competidores a opção de jogar novamente ou sair.
        if "*" not in palavra_oculta or numero_de_tentantivas == 0 or tentativa == palavra_chave:
            os.system("color 7")
            menu_final = (input("PRESS a opção desejada: JOGAR novamente(1), SAIR(2) "))
            if menu_final == "1":
                main()
            else :
                limpar_tela()
                print(f"{competidor} e {desafiante}, Mateus Lora agradece por jogar esse game, volte sempre!")
                quit()
            

def main():
    palavra_chave, dicas, competidor, desafiante = iniciar_jogo()
    jogo_da_forca(palavra_chave, dicas, competidor, desafiante)

main()

