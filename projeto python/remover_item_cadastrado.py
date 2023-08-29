def remover_item_cad():
    #            TELA DE PEDIDO
    lista_nova = []
    print("INSIRA O NÚMERO SERIAL DO ITEM A SER REMOVIDO: ")   
    #             ENTRADA DO USUÁRIO
    serie_item_remover = input("")
    #             LENDO ARQUIVO
    with open("cadastro.txt",'r') as lista_mover_item:
        for line in lista_mover_item:
            fabricante, modelo, numero_serial = line.strip().split(',')             
            if numero_serial == serie_item_remover:
    #              TELA INFORMANDO O PRODUTO SELECIONADO
                print(f"ITEM SELECIONADO: FABRICANTE: {fabricante}, MODELO: {modelo}, SERIAL: {numero_serial}")
    #              TELA PERGUNTANDO SE REALMENTE DESEJA EXCLUIR O ITEM
                print("------------- DESEJA REALMENTE EXCLUIR ESSE ITEM? --------------")
                print("[1].Sim")
                print("[2].Não")
    #              OPÇÕES DE ENTRADA   
                dado1 = input("")

                if dado1 == '1':
                    print("Sucesso! Seu item foi removido")
                    continue
             
                elif dado1 == '2':
                    continue    

            else:
                lista_nova.append(line.strip())

                                           
    with open("cadastro.txt",'w') as lista_mover_item:
        for linha in lista_nova:
            lista_mover_item.write(linha + '\n')


remover_item_cad()