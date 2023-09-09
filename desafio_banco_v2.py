import textwrap

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação inválida devido a falta de saldo na conta para realizar essa tarefa.")

    elif excedeu_limite:
        print("Operação inválida devido ao valor desejado para saque ser maior do que o limite acordado de R$500.")

    elif excedeu_saques:
        print("Operação inválida devido ao fato de que o número de saques é maior do que o acordado de 3 saques máximos.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação inválida, digite outro valor.")

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação inválida, digite outro valor.")

    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("Extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")


def cadastrar_usuario(usuarios):
    cpf = int(input("Digite o CPF do usuário (apenas números): "))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CPF indisponível.")
        return

    nome = input("Digite o nome do usuário: ")
    ddn = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço do usuário (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "ddn": ddn, "cpf": cpf, "endereco": endereco})


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Digite o CPF do usuário (apenas números): "))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado.")


def mostrar_contas(contas):

    for conta in contas:
        linha = f"""\n
            Agência: {conta['agencia']}
            C/C:     {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[cnu] = Cadastrar um novo usuário
[cnc] = Cadastrar uma nova conta
[mc] = Mostrar contas 
[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor desejado para depositar: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor desejado para sacar: "))
       
        saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES, )

    elif opcao == "e":
        mostrar_extrato(saldo, extrato = extrato)

    elif opcao == "cnu":
        cadastrar_usuario(usuarios)

    elif opcao == "cnc":
        numero_conta = len(contas) + 1
        conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "mc":
        mostrar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")