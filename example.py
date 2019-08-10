from tabulate_html import tabulate

headers = ['Nome', 'Idade', 'Cidade']

items = [
        ['Wilian', 21, 'Curitiba'],
        ]

document = tabulate(items, headers, 'Desenvolvedores')

with open('index.html', 'w') as f:
    f.write(document)