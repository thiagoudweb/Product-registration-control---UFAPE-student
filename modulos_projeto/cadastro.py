def cadastro_do_produto():
    fabricante_do_item = input("Digite a fabricante do produto: ")
    modelo_do_item = input("Digite o modelo do produto: ")
    codigo_serial = input("Digite o numero serial do produto: ")

#                   REGISTRANDO DADOS                   #
    with open("cadastro.txt","a") as cadastro_item:
          cadastro_item.write(f'{fabricante_do_item},{modelo_do_item},{codigo_serial}\n')
    
         
    print("Seu item foi cadastrado com sucesso!")


