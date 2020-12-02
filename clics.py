import requests, json
from lxml import html

def semshift(search_term):
    r = requests.get(f'https://clics.clld.org/parameters?sEcho=9&iColumns=7&sColumns=%23%2Cname%2C%23%2Ccount_varieties%2Ccount_colexifications%2Cinfomap%2Csubgraph&iDisplayStart=0&iDisplayLength=100&mDataProp_1=1&sSearch_1={search_term}',
                     headers={'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'})
    links = [html.fromstring(item[1]).attrib['href'] for item in json.loads(r.content)['aaData']]

    meanings = []
    for link in links:
        r2 = requests.get(link)
        tree = html.fromstring(r2.content)
        meanings += tree.xpath('//*[@class="Edge"]/text()')

    return list(map(str.lower, meanings))