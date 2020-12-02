import requests, json
from lxml import html

def semshift(search_term):
    r = requests.get(
        f'https://stedt.berkeley.edu/~stedt-cgi/rootcanal.pl/search/ajax?tbl=etyma&s={search_term}&f=&lg=&as_values_lg-auto=',
        headers={'accept': 'application/json'})
    meanings = []
    try:
        ids = [item[0] for item in json.loads(r.content)['data']]
        urls = [f'https://stedt.berkeley.edu/~stedt-cgi/rootcanal.pl/etymon/{id}' for id in ids]
        for url in urls:
            r2 = requests.get(url)
            tree2 = html.fromstring(r2.content)
            meanings += tree2.xpath('/html/body/table[2]/tbody/tr/td[5]/text()')
    except json.decoder.JSONDecodeError:
        pass

    return meanings