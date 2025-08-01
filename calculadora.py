def exibir_menu():
    print("Selecione uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calcular(opcao, num1, num2):
    if opcao == '1':
        return num1 + num2
    elif opcao == '2':
        return num1 - num2
    elif opcao == '3':
        return num1 * num2
    elif opcao == '4':
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2
    else:
        return "Opção inválida!"

def main():
    while True:
        exibir_menu()
        opcao = input("Digite sua opção (1-5): ")

        if opcao == '5':
            print("Saindo da calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        resultado = calcular(opcao, num1, num2)
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()