# Conversor de Números Romanos

class ConversorNumerosRomanos:
    def __init__(self):
        self.romano_para_inteiro = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        self.inteiro_para_romano = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def inteiro_para_romano_convert(self, numero):
        resultado = ''
        for valor, simbolo in self.inteiro_para_romano:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
    def romano_para_inteiro_convert(self, romano):
        resultado = 0
        ultimo_valor = 0
        for char in reversed(romano):
            valor = self.romano_para_inteiro[char]
            if valor < ultimo_valor:
                resultado -= valor
            else:
                resultado += valor
            ultimo_valor = valor
        return resultado
    
def menu():
    conversor = ConversorNumerosRomanos()
    print("=== Conversor de Números Romanos ===")
    print("1. Converter inteiro para romano")
    print("2. Converter romano para inteiro")
    print("0. Sair")

    while True:
        escolha = input("\n Escolha uma opção: ").strip()
        if escolha == '1':
            try:
                numero = int(input("Digite um número inteiro (1 a 3999): "))
                if 1 <= numero <= 3999:
                    print(f"Número romano: {conversor.inteiro_para_romano_convert(numero)}")
                else:
                    print("Por favor, insira um número entre 1 e 3999.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        elif escolha == '2':
            romano = input("Digite um número romano: ").strip().upper()
            try:
                print(f"Número inteiro: {conversor.romano_para_inteiro_convert(romano)}")
            except KeyError:
                print("Número romano inválido. Certifique-se de que está correto.")
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()