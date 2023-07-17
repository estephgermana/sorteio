import random

def realizar_sorteio(lista):
    sorteio = random.choice(lista)
    return sorteio
print('Olá, vou realizar o seu sorteio')
opcao = input("Deseja fazer um sorteio de nomes ou números? (n = nomes ou nu = números): ")

if opcao.lower() == 'n' or opcao.lower() == 'nomes':
    nomes = input("Informe os nomes que deseja separados por vírgula: ").split(',')
    sorteado = realizar_sorteio(nomes)
    print("O nome sorteado é:", sorteado.strip())

elif opcao.lower() == 'nu' or opcao.lower() == 'números':
    numeros = input("Informe os números que deseja sortear separados por vírgula: ").split(',')
    numeros = [int(num.strip()) for num in numeros]
    sorteado = realizar_sorteio(numeros)
    print("O número sorteado é:", sorteado)

else:
    print("Opção inválida. Tente novamente.")
