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
    valorTotal = float(0)
    valorAnterior = 0
    valorPago = 0
    resposta = "N"
    itens = 1
    troco = 0
    x = "N"
    numeroClientes = 0

    while x == "N":

        while resposta == "N":
            
            print("(Caso o valor for digitado errado digite -1 para alterar e caso deseje encerrar digite 0)")
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
        
        #itens = 1
        resposta = "N"
        print(f"\nVenda finalizada com {itens-1} itens.")
        print(f"O valor total foi {valorTotal} R$")
        valorPago = float(input("Valor pago: "))

        # PAGAMENTO / PAYMENT

        if valorTotal > caixa:
            print("\nNão há troco")

        else:

            troco = valorPago - valorTotal
            caixa -= troco
            print(f"\nTroco: {troco:.2f}")

            if troco >= duzentosDisponivel:

                while troco >= 200:

                    duzentosDisponivel -= 1
                    duzentosUsadas += 1
                    troco -= 200

                print(f"{duzentosUsadas} notas de 200")

            if troco >= cemDisponivel:
                    
                while troco >= 100:

                    cemDisponivel -= 1
                    cemUsadas += 1
                    troco -= 100

                print(f"{cemUsadas} notas de 100")

            if troco >= cinquentaDisponivel:
                    
                while troco >= 50:

                    cinquentaDisponivel -= 1
                    cinquentaUsadas =+ 1
                    troco -= 50
                    
                print(f"{cinquentaUsadas} notas de 50")

            if troco >= dezDisponivel:

                while troco >= 10:

                    dezDisponivel -= 1
                    dezUsadas += 1
                    troco -= 10

                print(f"{dezUsadas} notas de 10")

            if troco >= cincoDisponivel:
                    
                while troco >= 5:

                    cincoDisponivel -= 1
                    cincoUsadas += 1
                    troco -= 5

                print(f"{cincoUsadas} notas de 5")

            if troco >= umRealDisponivel:
                    
                while troco >= 1:

                    umRealDisponivel -= 1
                    umRealUsadas += 1
                    troco -= 1

                print(f"{umRealUsadas} moedas de 1")

            if troco >= cinquentaCentavosDisponivel:
                    
                while troco >= 0.5:

                    cinquentaCentavosDisponivel -= 1
                    cinquentaCentavosUsadas += 1
                    troco -= 0.5

                print(f"{cinquentaCentavosUsadas} moedas de 0.50")

        numeroClientes += 1
        valorTotal += valor
        print()
        x = input("Deseja fechar o caixa [S/N]: ").upper()

    print(f"\nRestante no caixa R${caixa - valorTotal}")
    print(f"Numero de clientes atendidos {numeroClientes}")
    print("Até mais...")
