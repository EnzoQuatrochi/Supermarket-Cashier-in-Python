# SENHA = 2987 / PASSWORD = 2987

tentativas = 3
senha = 0

print("Bem vindo!")
senha = int(input("Digite a senha: "))

while senha != 2987:

    tentativas -=1
    print(f"\nSenha incorreta")
    print(f"Voce tem mais {tentativas} tentativas")
    print()
    senha = int(input("Digite a senha: "))
        
    if tentativas == 1:

        print(f"\nO sistema será reiniciado")
        print()
        break

if senha == 2987:
    print(f"\nSenha correta")
    print("Caixa aberto!!!")
    print()

    #  QUANTIA DE NOTAS DISPONIVEIS / QUANTITY OF NOTES AVAILABLE

    duzentosDisponivel = 2
    cemDisponivel = 4
    cinquentaDisponivel = 6
    dezDisponivel = 10
    cincoDisponivel = 10
    umRealDisponivel = 5
    cinquentaCentavosDisponivel = 20

    # QUANTIDADE DE NOTAS QUE SERÃO UTILIZADAS NO TROCO / QUANTITY OF MONEY THAT WILL BE USED IN THE CHANGE

    duzentosUsadas = 0
    cemUsadas = 0
    cinquentaUsadas = 0
    dezUsadas = 0
    cincoUsadas = 0
    umRealUsadas = 0
    cinquentaCentavosUsadas = 0

    # QUANTIDADE DE DINHEIRO = 1280 / QUANTITY OF MONEY = R$1280
    '''
    2 * 200 = 400
    4 * 100 = 400
    6 * 50 = 300
    10 * 10 = 100
    10 * 5 = 50
    20 * 1 = 20
    20 * 0.5 = 10
    '''
    caixa = float(1280)
    valor = int(0)
    valorTotal = int(0)
    valorAnterior = 0
    valorPago = 0
    resposta = "N"
    itens = 1
    troco = 0
    x = "S"
    numeroClientes = 0

    while x == "S":

        while resposta == "N":
                
            valor = float(input(f"Diga o valor do item {itens}: "))

            #resposta = input("Deseja inserir mais algum valor [S/N]").upper()

            if valor == -1:

                valorTotal -= valorAnterior

                valor = int(input(f"Digite o valor correto do item {itens-1}: "))

            if valor == 0:

                print()
                resposta = input("Deseja mesmo encerrar? [S/N]").upper()

            itens +=1
            valorTotal += valor
            valorAnterior = valor
        
        itens = 1
        resposta = "N"
        print(f"\nVenda finalizada com {itens-1} itens.")
        print(f"O valor total foi {valorTotal} R$")
        valorPago = int(input("Valor pago: "))

        # PAGAMENTO / PAYMENT

        if valorTotal > caixa:
            print("\nNão há troco")

        else:

            troco = valorPago - valorTotal
            caixa -= troco
            print(f"\nTroco: {troco:.2f}")




