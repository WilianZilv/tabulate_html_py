def node(tag, child, prop=''):
    return "<{0} {2}>{1}</{0}>".format(tag, child, prop)

def finish(child, title):

    with open('style.css', 'r') as f:
        style = node('style', f.read())
    
    head = node('head', node('title', title) + style)
    body = node('body', node('h2', title) + child)
    
    document = '<!DOCTYPE html>'+node('html', head + body)
    
    with open('table.html', 'w') as f:
        f.write(document)
        f.close()

def tabulate(items, headers, title):
    
    table_headers = node('tr', "".join([node('th', label) for label in headers]))
    table_items = "".join([node('tr', "".join([node('td', val) for val in values])) for values in items])
    
    table = node('table', table_headers + table_items)
    
    finish(table, title)
