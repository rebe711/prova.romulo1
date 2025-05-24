def q1():
    anoPrimeira = int(input("Digite o ano inicial: "), 10) 
    intervalo = int(input("Digite o intervalo: "))

    for i in range(1, 5):
        anoDose = anoPrimeira + i * intervalo
        print(anoDose, end = ' ')

def q2():
    
    while True:
        numero = int(input("Digite um número (ou -1 para sair): "))

        if numero == -1:
            break 

        elif numero < 2:
            print("Não")
            continue
        else:     
            for i in range(2, numero):
                if numero % i == 0:
                    print("Não")
                    break
            else:
                print("Primo")

def q3():
    valorDoado = 0
    valorTotal = 0
    quantidade = 0

    while True:
        valorDoado = float(input("Digite o valor doado: "))

        if valorDoado == -1:
            break

    quantidade += 1
    valorTotal += valorDoado

    if quantidade > 0:
        media = valorTotal / quantidade
        print(f"Total: {valorTotal:.2f}")
        print(f"Quantidade de doações: {quantidade}")
        print(f"Média: {media:.2f}")
    else:
        print("Nenhuma doação foi feita.")

def q4():
    dias = int(input("Digite os dias: "))
    km = float(input("Digite os km rodados: "))

    custoFixo = dias * 90
    cotaKm = dias * 100

    kmExtra = km - cotaKm
    if kmExtra > 0:
        custoKmExtra = kmExtra * 12
    else:
        custoKmExtra = 0

    total = custoKmExtra + custoFixo
    print(f"{total:.2f}")  


def q5():
    escala = input("Escala (C/F/K): ").upper()     
    temp = float(input("Digite a temperatura: "))  

    if escala == 'C':
        fahr = (temp * 9/5) + 32
        kelv = temp + 273.15
    elif escala == 'F':
        cels = (temp - 32) * 5/9
        kelv = cels + 273.15
    elif escala == 'K':
        cels = temp - 273.15
        fahr = (cels * 9/5) + 32
    else:
        print("Escala inválida! Use C, F ou K.")
        exit()

    print(f"{temp:.1f}°{escala}")
    if escala != 'C':
        print(f"{cels:.1f}°C")
    if escala != 'F':
        print(f"{fahr:.1f}°F")
    if escala != 'K':
        print(f"{kelv:.1f}K")

if __name__=="__main__":
    q5()