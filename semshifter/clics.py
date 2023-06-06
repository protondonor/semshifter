import requests, json
from lxml import html

from semshifter.helper import multi_request


def semshift(search_term):
    r = requests.get(
        f'https://clics.clld.org/parameters?sEcho=9&iColumns=7&sColumns=%23%2Cname%2C%23%2Ccount_varieties%2Ccount_colexifications%2Cinfomap%2Csubgraph&iDisplayStart=0&iDisplayLength=100&mDataProp_1=1&sSearch_1={search_term}',
        headers={'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'})
    urls = [html.fromstring(item[1]).attrib['href'] for item in json.loads(r.content)['aaData']]

    results = multi_request(urls)
    meanings = []
    for result in results:
        tree = html.fromstring(result.content)
        meanings += tree.xpath('//*[@class="Edge"]/text()')

    return meanings


def reverse(search_term):
    # CLICS is bidirectional
    return semshift(search_term)
