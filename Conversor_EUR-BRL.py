from currency_converter import CurrencyConverter
from datetime import date


def lin(tam=30):
    return print('-' * tam)


def moeda(preco=float(0), simbolo='R$'):
    return f'{simbolo} {preco:.2f}'.replace('.', ',')


def leia_din(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um valor válido!\033[m')
            continue
        else:
            return num


c = CurrencyConverter()
lin()
print(f'{"CONVERSOR EUR-BRL":^30}\n{str(date.today()):^30}')
lin()
eur = leia_din('Euros = € ')
print(f'{"Real ="} {moeda(preco=c.convert(eur, "EUR", "BRL"))}')
