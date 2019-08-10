from tabulate_html import tabulate

headers = ['Nome', 'Idade', 'Cidade']

items = [
        ['Wilian', 21, 'Curitiba'],
        ]

tabulate(items, headers, 'Desenvolvedores')