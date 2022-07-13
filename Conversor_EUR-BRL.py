from currency_converter import CurrencyConverter
from datetime import date


def lin(tam=30):
    return print('-' * tam)


def moeda(preco=0, symb='R$'):
    return f'{symb} {preco:.2f}'.replace('.', ',')


def leiaDin2(txt):
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
print(f'{str(date.today()):^30}')
lin()
eur = leiaDin2('Euros = € ')
print(f'{"Real ="} {moeda(preco=c.convert(eur, "EUR", "BRL"))}')
