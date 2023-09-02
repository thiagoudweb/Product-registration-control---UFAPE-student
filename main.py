############ TELA DE LOGUIN ------
import modulos_projeto.cadastro as cadastro
import modulos_projeto.mod_buscar as mod_buscar
import modulos_projeto.editar_propriedades as editar_propriedades
import limpar_terminal

def tela_de_opcao():
    print("'''''''' ESCOLHA UMA OPÇÃO ''''''''''")
    print("[1].CADASTRAR ITEM")
    print("[2].BUSCAR ITEM")
    print("[3].EDITAR ITENS CADASTRADOS")
    print("[4].REMOVER ITEM CADASTRADO")
    print("[5].SAIR")


######## ENTRADA DE DADOS ------

def condicionais_do_usuario(opcao):
    if opcao == '1':
       cadastro.cadastro_do_produto()
    
    elif opcao == '2':
       mod_buscar.buscar_itens()
            
    elif opcao == '3':
        editar_propriedades.editar_propri_item()

    elif opcao == '4':
        print("Você escolheu a opção 4")  


################ TELA INICIAL 

while True:
    limpar_terminal.limpar_terminal()
    tela_de_opcao()
    entrada_usuario = input("Digite uma opção:")
    condicionais_do_usuario(entrada_usuario)
    if entrada_usuario == '5':
       break
   

   