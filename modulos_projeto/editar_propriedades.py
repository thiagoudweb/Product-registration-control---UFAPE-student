def editar_propri_item():
    
    #                GUARDANDO LINHAS TXT PARA NOVA ESCRITA
    novas_linhas = []
    #                TELA DE PEDIDO
    print("DIGITE O N° SERIAL DO ITEM A SER ATUALIZADO:")
    
    #                ENTRADA DO USUARIO
    entrada_usuario = input("")
    #                BUSCANDO ITEM 
    with open("cadastro.txt", "r") as editar_propriedade_item:       
           for line in editar_propriedade_item:          
              fabricante, modelo, serial_do_item = line.strip().split(',')          
              if serial_do_item == entrada_usuario:
    #                SALVANDO PROPRIEDADES DO ITEM ENCONTRADO
                lista_item = [fabricante,modelo,serial_do_item]
    #                MOSTRANDO ITEM ESCOLHIDO
                print(f"PRODUTO SELECIONADO: 'FABRICANTE': {fabricante}, 'MODELO': {modelo}, ' N° SERIAL: {serial_do_item} ")
    #                TELA DE ESCOLHA                 
                print("ESCOLHA UMA PROPRIEDADE DO SEU PRODUTO PARA SER ALTERADO:")
                print("[1]. ATUALIZAR FABRICANTE ")
                print("[2]. ATUALIZAR MODELO")
                print("[3]. ATUALIZAR N° SERIAL") 
    
    #                ENTRADA DO USUÁRIO 
                entrada_usuario_escolha =  int(input("ESCOLHA UMA OPÇÃO: "))
    
    #                CONDICIONAIS DE ENTRADA            
               
                if entrada_usuario_escolha == 1:
                    print(f"Atualmente o fabricante desse item é {fabricante}")
                    dado1 = input("Digite o novo fabricante que você quer inserir:")
                    lista_item[0] = dado1
                    nova_linha_txt = ','.join(lista_item)
                    novas_linhas.append(nova_linha_txt)
                    print("Sucesso! Seu item foi atualizado com sucesso!")

                elif entrada_usuario_escolha == 2:
                   
                    print(f"Atualmente o modelo desse item é {modelo}")
                    dado2 = input("Digite o novo fabricante que você quer inserir:")
                    lista_item[1] = dado2
                    nova_linha_txt = ','.join(lista_item)
                    novas_linhas.append(nova_linha_txt)
                    print("Sucesso! Seu item foi atualizado com sucesso!")    
                
                elif entrada_usuario_escolha == 3:

                    print(f"Atualmente o modelo desse item é {serial_do_item}")
                    dado3 = input("Digite o novo fabricante que você quer inserir:")
                    lista_item[2] = dado3
                    nova_linha_txt = ','.join(lista_item)
                    novas_linhas.append(nova_linha_txt)
                    print("Sucesso! Seu item foi atualizado com sucesso!")
                                                                   
              else:
                    novas_linhas.append(line.strip())
                    

#                       ESCREVENDO LINHA
    
    with open("cadastro.txt", "w") as editar_propriedade_item:
        for linha in novas_linhas:
             editar_propriedade_item.write(linha + '\n')    
                    
    return  




