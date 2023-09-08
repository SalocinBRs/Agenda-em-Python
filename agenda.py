AGENDA = {}


def deletar_contato(contato):
    del AGENDA[contato]


def mostrar_contatos(agenda):
    if len(AGENDA) > 0:
        print("-" * 30)
        for contatos in agenda:
            print(f"Nome: {contatos}")
            print("Telefone:", agenda[contatos]["telefone"])
            print("Email:", agenda[contatos]["email"])
            print("endereço:", agenda[contatos]["endereço"])
            print("-" * 30)
    else:
        print("A lista está vazia")


def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
    "telefone": telefone,
    "email": email,
    "endereço": endereco
    }
    exportar_contatos()
    print('-' * 30)
    print(contato)
    print('Telefone: ',AGENDA[contato]["telefone"])
    print('Email: ',AGENDA[contato]["email"])
    print('Endereço: ',AGENDA[contato]["endereço"])


def buscar_contato():
    while True:
        try:
            nome = str(input("Qual o nome: "))
            print('Telefone: ',AGENDA[nome]["telefone"])
            print('Email: ',AGENDA[nome]["email"])
            print('Endereço: ',AGENDA[nome]["endereço"])
            break
        except KeyError:
            print("Esse contato não existe")


def exportar_contatos():
    try:
        with open('contatos.csv', 'w', encoding="utf-8") as arquivos:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereço']
                arquivos.write(f"{contato},{telefone},{email},{endereco}\n")
    except Exception as error:
        print("nao foi")
        print(error)

with open('contatos.csv', encoding="utf-8") as teste:
    linhas = teste.readlines()
    for linha in linhas:
        detalhes = linha.strip().split(',')
        contato = detalhes[0]
        telefone = detalhes[1]
        email = detalhes[2]
        endereco = detalhes[3]
        AGENDA[contato] = {
    "telefone": telefone,
    "email": email,
    "endereço": endereco
    }

while True:
    print("~~" * 20)
    print("MENU ALPHA")
    print("~~" * 20)
    print("Para adicionar/editar um contato digite 0\nPara buscar um contato digite 1")
    print("Para exibir todos os contatos digite 2\nPara excluir um contato digite 3")
    print("Para exportar os arquivos em CSV digite 4")
    print("Para sair digite 9")
    resposta = int(input(""))
    if resposta in [0]:
        while True:
            try:
                contato = input("Qual o nome: ")
                telefone = int(input("Qual o numero: "))
                email = input("Qual o email: ")
                endereco = input("Qual o endereço: ")
                incluir_editar_contatos(contato, telefone, email, endereco)
                break
            except ValueError:
                print("Apenas numeros são aceitos no telefone")

    if resposta in [1]:
        buscar_contato()

    if resposta in [2]:
        mostrar_contatos(AGENDA)

    if resposta in [3]:
        while True:
            try:
                contato = input('Qual contato deverá ser deletado: ')
                deletar_contato(contato)
                break
            except KeyError:
                print("contato inválido")
    if resposta in [4]:
        exportar_contatos()

    if resposta in [9]:
        break
    elif resposta not in [0,1,2,3,4,9]:
        print("~~" * 20)
        print("Opção inválida")
print("FIM")
teste.close()
