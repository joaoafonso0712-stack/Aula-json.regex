
import os
import re
import json as manipjson

filename = R"D:\DEV\Python\PI PL 0925\10793\dicionario.json"
numero = 0
idade=""
nif=""
morada="" # {"idade": 12, "morada": "Rua do desespero"}
opc1=""

if os.path.exists(filename):
    with open(filename, "r", encoding='utf-8') as file:
        dicpessoa = manipjson.load(file)
        
while True:
    print("MENU: ")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Gravar file")
    print("5 - Sair sem guardar")
    opc = input("Opção: ")

    match opc:
        case "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            telefone = input("Telefone: ")
            nif = input("NIF: ")
            compra = float(input("Compra: "))
            
            if compra >= 100 and compra <= 200:
                desconto = 0.05
            elif compra >= 200 and compra <= 500:
                desconto = 0.10
            elif compra > 500:
                desconto = 0.15
            else:
                desconto = 0

            divfinal = compra * desconto
        case "2":
            print(nome)
            print(idade)
            print(telefone)
            print(nif)
            print(compra)
        case "3":
            print("Remover")
        case "4":
            dicpessoa = {
                "Nome": nome,
                "Idade": idade,
                "Telefone": telefone,
                "NIF": nif,
                "Compra": compra
            }
            
            with open(filename, "w", encoding='utf-8') as file:
                #json.dump salva o dicionário no arquivo como texto JSON
                #indent=4 deixa o JSON formatado
                #f: é o file handler, o arquivo aberto em modo escrita "w"
                #ensure_ascii=False permite acentos e caracteres especiais
                manipjson.dump(dicpessoa, file, indent=4, ensure_ascii=False)
                break
        case "5":
            sair=1
        case _:
            print("Opção inválida")
