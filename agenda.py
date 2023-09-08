AGENDA = {}


def deletar_contato(perfil):
    del AGENDA[perfil]
    print(f"{perfil} deletado com Sucesso")


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


def editar_contatos(a, b, c, d):
    AGENDA[a] = {
    "telefone": b,
    "email": c,
    "endereço": d
    }
    exportar_contatos()
    print('-' * 30)
    print(contato)
    print("Editado com sucesso")


def incluir_contatos(a, b, c, d):
    AGENDA[a] = {
    "telefone": b,
    "email": c,
    "endereço": d
    }
    exportar_contatos()
    print('-' * 30)
    print(contato)
    print("Incluido com sucesso")


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
            for nome in AGENDA:
                tel = AGENDA[nome]['telefone']
                Email = AGENDA[nome]['email']
                local = AGENDA[nome]['endereço']
                arquivos.write(f"{nome},{tel},{Email},{local}\n")
    except FileNotFoundError:
        print("Arquivo não encontrado")


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
    print("0 - Para adicionar um contato \n1 - Para buscar um contato")
    print("2 - Para exibir todos os contatos \n3 - Para excluir um contato ")
    print("4 - Para exportar os arquivos em CSV\n5 - Para editar contatos ")
    print("9 - Para sair")
    resposta = int(input(""))
    try:
        if resposta in [0]:
            while True:
                try:
                    contato = input("Qual o nome: ")
                    telefone = int(input("Qual o numero: "))
                    email = input("Qual o email: ")
                    endereco = input("Qual o endereço: ")
                    incluir_contatos(contato, telefone, email, endereco)
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

        if resposta in [5]:
            while True:
                try:
                    contato = input("Qual o nome: ")
                    telefone = int(input("Qual o numero: "))
                    email = input("Qual o email: ")
                    endereco = input("Qual o endereço: ")
                    editar_contatos(contato, telefone, email, endereco)
                    break
                except ValueError:
                    print("Apenas numeros são aceitos no telefone")

        if resposta in [9]:
            break
        elif resposta not in [0,1,2,3,4,5,9]:
            print("~~" * 20)
            print("Opção inválida")
    except KeyError:
        print("tente novamente")

print("FIM")
