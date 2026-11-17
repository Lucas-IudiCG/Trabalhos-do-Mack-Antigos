import random

# ==========================================
# 1. Função: Verificar se o vetor é crescente (2.2 Vetor.py)
# ==========================================
def Crescente():
    Size = int(input("Digite o tamanho do vetor: "))
    vet = [0] * Size
    H = Size - 1
    X = 0
    while H > -1:
        vet[X] = int(input("Digite um Número: "))
        H = H - 1
        X = X + 1
    
    H2 = len(vet)
    H2 = H2 - 1
    H3 = H2
    Y = 0
    final = True
    while H2 > -1 and Y < H3 and final == True:
        if vet[Y] < vet[Y + 1]:
            H2 = H2 - 1
            Y = Y + 1
        else:
            final = False

    if final == False:
        print("Não é crescente")
    else:
        print("É crescente")
        
    input("\nPressione Enter para continuar...")


# ==========================================
# 2. Função: União de Vetores (2.0 Vetor Uniao.py)
# ==========================================
def geraVetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1, 10)
    return vetor


def uniao(A, B):
    Solucao = " "
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                Solucao = Solucao + str(A[i]) + " "
    return Solucao


def ExecutarUniao():
    Size1 = int(input("Tamanho do Primeiro vetor: "))
    Size2 = int(input("Tamanho do Segundo vetor: "))
    A = [0] * Size1
    B = [0] * Size2

    print("Vetor B:", geraVetor(B))
    print("Vetor A:", geraVetor(A))
    print("União (elementos em comum):", uniao(A, B))
    
    input("\nPressione Enter para continuar...")


# ==========================================
# 3. Função: Verificar se é crescente - Versão 2 (2.0 Vetor.py)
# ==========================================
def GeraVetorCrescente():
    Size = int(input("Digite o tamanho do vetor: "))
    vet = [0] * Size
    H = Size - 1
    X = 0
    while H > -1:
        vet[X] = int(input("Digite um Número: "))
        H = H - 1
        X = X + 1
        
    H2 = len(vet)
    H2 = H2 - 1
    H3 = H2
    Y = 0
    final = True
    while H2 > -1 and Y < H3 and final == True:
        if vet[Y] < vet[Y + 1]:
            H2 = H2 - 1
            Y = Y + 1
        else:
            final = False

    if final == False:
        print("Não é crescente")
    else:
        print("É crescente")
        
    input("\nPressione Enter para continuar...")


# ==========================================
# 4. Função: Diferença de Vetores (2.0 Vetor Diferenca.py)
# ==========================================
def dif(A, B):
    Solucao = " "
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] != B[j]:
                Solucao = Solucao + str(A[i]) + " "
    return Solucao


def ExecutarDiferenca():
    Size1 = int(input("Tamanho do Primeiro vetor: "))
    Size2 = int(input("Tamanho do Segundo vetor: "))
    A = [0] * Size1
    B = [0] * Size2

    print("Vetor A:", geraVetor(A))
    print("Vetor B:", geraVetor(B))
    print("Diferença:", dif(A, B))
    
    input("\nPressione Enter para continuar...")


# ==========================================
# Menu Principal
# ==========================================
def main():
    while True:
        print("\n=== MENU DE PROGRAMAS ===")
        print("1. Verificar Crescente (2.2 Vetor)")
        print("2. União de Vetores (2.0 Vetor Uniao)")
        print("3. Verificar Crescente - Versão 2 (2.0 Vetor)")
        print("4. Diferença de Vetores (2.0 Vetor Diferenca)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Crescente()
        elif opcao == "2":
            ExecutarUniao()
        elif opcao == "3":
            GeraVetorCrescente()
        elif opcao == "4":
            ExecutarDiferenca()
        elif opcao == "0":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
