# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Joao luiz leao bueno, joaollb@al.insper.edu.br
# - aluno B: Raphael Butori, raphaeljb@al.insper.edu.br
# - aluno C: Rodrigo Senatti Mattar rodrigosm11@al.insper.edu.br

import random
from random import randint  
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()



    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    #Coloca inventario
    forcadic = dict()
    inventario = ['nada']
    forcadic['forca'] = 0 
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        monstro= False
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
      
        if nome_cenario_atual!="inicio":
            monstro=bool(randint(0,1))
            
        temitem = randint(0,2)
        opcoesitens = ['espada', 'kit medico']
        titulo=cenario_atual['titulo']
        print(titulo)
        print('-'* len(titulo))
        descricao=cenario_atual['descricao']
        print(descricao)
        print('Inventario: ' ,inventario)
        opcoes = cenario_atual['opcoes'] 
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            print('voce morreu')
            game_over = True
        else:
            #funcao que da opcoes de itens no inventario
            def embaralha_itens_e_adiciona_ao_inventario (opcoesitens):
                opcoespegar = []
                aleatorio1 = random.choice(opcoesitens)
                aleatorio2 = random.choice(opcoesitens)
                while aleatorio1 == aleatorio2:
                    aleatorio1 = random.choice(opcoesitens)
                opcoespegar.append(aleatorio1)
                opcoespegar.append(aleatorio2)
                print('Voce encontrou 2 itens nesta sala:', opcoespegar)
                resp = input('Digite o nome do item que voce deseja adicionar ao seu inventario: ')
                if resp == aleatorio1 or resp == aleatorio2:
                    if 'nada' in inventario:
                        inventario[0]=resp
                    else:
                        inventario.append(resp)
                else:
                    print('voce nao pegou nada')
                print ('novo inventario',inventario)
                
            if temitem==1:
                embaralha_itens_e_adiciona_ao_inventario(opcoesitens)
 
            #Big boss eh luta final
           
        
            local_revive=["biblioteca","inicio","andar professor"]
            #Reviver 
            if not game_over:
                def reviver (x):
                    for armas1 in x:
                        if armas1 == 'kit medico':
                            print('Voce morreu, mas voce possui um kit medico! ')
                            resposta = input('Voce deseja usar para reviver?(voce perdera todos seus itens no processo!): ')
                            if resposta == 'sim'.lower():
                                game_over = False 
                                i=0
                                while i<len(inventario):
                                    del(inventario[i])
                                    i+=1
                                escolha1 = input('Aonde voce quer renascer?')
                                if escolha1 in cenario_atual:
                                    nome_cenario_atual = escolha1
                                    if temitem:
                                        embaralha_itens_e_adiciona_ao_inventario(opcoesitens)
                            else:   
                                        game_over = True


            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
       
            if not game_over:    #colocando o monstro
                if monstro:
                    print('Tem um veterano no local!!')
                while monstro:
                    print('sim: quero lutar' )
                    print("nao: quero fugir pra minha mamae")
                    f=str(input('Voce quer lutar? '))
                    if f!='nao':
                            if 'ak-47'in inventario or 'rpg'in inventario or  'espada'in inventario:
                                print('Voce arrebentou o veterano')
                                forcadic['forca']+= 1 
                                print(forcadic)
                              
                                break
                            else:
                                print( "vai ter que ser na marra")
                                luta = bool(randint(0,1))
                                if luta:
                                    print('Voce derrotou o veterano')
                                    forcadic['forca']+= 1
                                    print(forcadic)
                        
                                    break
                         
                                else:
                                    game_over=True
                                    print('Voce foi destroçado pelo veterano')
                                    print('voce morreu')
                                    reviver(inventario)
                            
                                monstro=False
                                break
                    else:
                        print('o veterano te zoa de covarde , mas ok , segue o jogo')
                        break
                if not game_over:
                    if forcadic['forca'] >= 3:
                        
                        opcaodeluta = input('Voce atingiu a forca maxima, agora voce obteve acesso a sala extra: a batalha final.deseja se teletransportar para a sala? ')
                        if opcaodeluta == 'sim':
                                print('Voce se deparou com o big boss, a batalha final, agora voce pode escolher um item do inventario para usar na batalha')
                                print(inventario)
                                opcaodearma= input('Digite a a arma que voce deseja usar na luta: ')
                                if opcaodearma == 'rpg'or opcaodearma=='granada':
                                   
                                    print('bOOOOooooOoooOOOOoOOOOM')
                                    print('Voce ganhou a luta final!')
                                    print('Voce destruiu o bigboss utilizando a', opcaodearma)
                                    print('com a queda do big boss e derrota dos veteranos em seu caminho voce adquiriu')
                                    print('.')
                                    print('.')
                                    print('.')
                                    print('.')
                                    print('.')
                                    print('habilidade de argumentação!!!')
                                    print('unindo sua mais nova qualidade de argumentacao com seu charme unico, voce conseguiu conquistar a bencao de Mestre Toshi!')
                                    print('adiando a entrega do ep voce se torna o menino mais popular da turma!')
                                    print('FORÇA=100000000000000000000000000000')
                                    print('parabens!!!!!')
                                    game_over=True    
                                
                                    
                                elif opcaodearma == 'banana'or opcaodearma=='kit medico' or opcaodearma=='ak-47' or opcaodearma=='espada':
                                   
                                    print('Voce perdeu a luta!')
                                    print(opcaodearma, 'nao foi suficiente para superar o poder do bigboss!!')
                                    print('voce morreu') 
                                    game_over=True    
                                
                
                
            if not game_over:   
                for a,b in opcoes.items():
                    print(' opcao-:{0}:{1}'.format(a,b))
                e=str(input('Para onde voce deseja ir? '))
                escolha = e
               

                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    print('voce morreu')
                    game_over=True
   
if __name__ == "__main__":
    main()