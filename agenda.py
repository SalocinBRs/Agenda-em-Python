AGENDA = {}

AGENDA["Nicolas"] = {
    "telefone": "999252508",
    "email": "nv15983@gmail.com",
    "endereço": "rua principal 1"
}
AGENDA["Maria"] = {
    "telefone": "999248613",
    "email": "mv7983@gmail.com",
    "endereço": "rua principal 2"
}
def deletar_contato(contato):
    del AGENDA[contato]


def mostrar_contatos(agenda):
    print("-" * 30)
    for contatos in agenda:
        print(f"Nome: {contatos}")
        print("Telefone:", agenda[contatos]["telefone"])
        print("Email:", agenda[contatos]["email"])
        print("endereço:", agenda[contatos]["endereço"])
        print("-" * 30)


def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
    "telefone": telefone,
    "email": email,
    "endereço": endereco
    }
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

while True:
    print("~~" * 20)
    print("MENU ALPHA")
    print("~~" * 20)
    print("Para adicionar/editar um contato digite 0\nPara buscar um contato digite 1")
    print("Para exibir todos os contatos digite 2\nPara excluir um contato digite 3")
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
            except:
                print("contato inválido")
    if resposta in [9]:
        break
print("FIM")
