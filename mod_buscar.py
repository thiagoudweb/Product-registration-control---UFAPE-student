def buscar_itens():
    
    #                TELA DE PEDIDO
    print("------ ESCOLHA UMA OPÇÃO ------")
    print("[1]. Buscar item por N° de série ")
    print("[2]. Buscar item por modelo ")

    #                DADOS DO USUARIO
    opcao_busca_item = int(input())
    
    #                BUSCANDO POR NUMERO DE SÉRIE 
    if (opcao_busca_item == 1):    
         n_serial = input("Digite o numero de série do produto: ")     
         with open("cadastro.txt", "r") as cadastro_item:       
           for line in cadastro_item:          
              fabricante, modelo, serial_do_item = line.strip().split(',')          
              if serial_do_item == n_serial:          
                return print(f"O item encontrado foi: Fabricante: {fabricante}, Modelo: {modelo}, Serial: {serial_do_item}")

    #                BUSCANDO POR MODELO            
    
    elif (opcao_busca_item == 2):
         modelo_prod = input("Digite o modelo do produto: ")     
         with open("cadastro.txt", "r") as cadastro_item:       
           for line in cadastro_item:          
              fabricante, modelo, serial_do_item = line.strip().split(',')          
              if modelo == modelo_prod:          
                return print(f"Fabricante: {fabricante}, Modelo: {modelo}, Serial: {serial_do_item}") 


   #                  SEM RESULTADO
    else:
      return buscar_itens()


   


    