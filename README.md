# tabulate_html.py
A python script to automatically create a table in html

# How to use it?
Folow this example:
<br/>
<br/>
<code>
from tabulate_html import tabulate

headers = ['Nome', 'Idade', 'Cidade']

items = [
        ['Wilian', 21, 'Curitiba'],
        ]

tabulate(items, headers, 'Desenvolvedores')
</code>

