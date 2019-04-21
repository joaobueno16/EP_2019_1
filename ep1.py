# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br
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

vida=3
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
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        monstro= False
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
      
        if nome_cenario_atual!="inicio":
            monstro=bool(randint(0,1))

        
        temitem = bool(randint(0,1))
        opcoesitens = ['espada', 'kit medico', 'granada', 'ak-47','rpg', 'Banana']
        inventario = []
        titulo=cenario_atual['titulo']
        print(titulo)
        print('-'* len(titulo))
        descricao=cenario_atual['descricao']
        print(descricao)
        print(inventario)
        opcoes = cenario_atual['opcoes'] 
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
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
                    if resp == aleatorio1 or aleatorio2:
                        inventario.append(resp)
                    break
            for a,b in opcoes.items():
                print('{0}:{1}'.format(a,b))
                if temitem:
                    embaralha_itens_e_adiciona_ao_inventario(opcoesitens)

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
                            
                
                #colocando o monstro
            if monstro:
                print('Tem um veterano no local!!')
            while monstro:
                print('sim: quero lutar' )
                print("nao: quero fugir pra minha mamae")
                f=str(input('Voce quer lutar? '))
                if f!='nao':
                    luta=bool(randint(0,1))
                    for armas in inventario:
                        if armas == 'AK-47' or 'rpg' or  'espada':
                            luta = True    
                    print(luta)
                    if luta:
                        print('Voce arrebentou o veterano')
                        break
                    else:
                        game_over=True
                        print('Voce foi destroçado pelo veterano')
                        
                    monstro=False
                    break
                else:
                    break
            if not game_over:                
                e=str(input('Para onde voce deseja ir? '))
                escolha = e

                if escolha in opcoes:
                    temitem = bool(randint(0,1))
                    nome_cenario_atual = escolha
                    if temitem:
                        embaralha_itens_e_adiciona_ao_inventario(opcoesitens)
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True

    print("Você morreu!")
    
      


if __name__ == "__main__":
    main()
   
