import requests, json
from lxml import html
from helper import multi_request


def semshift(search_term):
    r = requests.get(
        f'https://stedt.berkeley.edu/~stedt-cgi/rootcanal.pl/search/ajax?tbl=etyma&s={search_term}&f=&lg=&as_values_lg-auto=',
        headers={'accept': 'application/json'})
    meanings = []
    try:
        ids = [item[0] for item in json.loads(r.content)['data']]

        if len(ids) == 0:
            return []
        urls = [f'https://stedt.berkeley.edu/~stedt-cgi/rootcanal.pl/etymon/{id}' for id in ids]
        results = multi_request(urls)

        for r2 in results:
            tree2 = html.fromstring(r2.content)
            meanings += tree2.xpath('/html/body/table[2]/tbody/tr/td[5]/text()')

    except json.decoder.JSONDecodeError:
        pass

    return list(set(meanings))