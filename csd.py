import requests, json
from lxml import html

from helper import multi_request


def lemmas(search_term):
    r = requests.get(
        f'https://csd.clld.org/values?sEcho=86&iColumns=6&sColumns=lemma%2Clanguage%2Cname%2Cphonetic%2Cdescription%2Ccomment&sSearch_4={search_term}&bRegex_4=false&bSearchable_4=true',
        headers={'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'})
    return [item[4] for item in json.loads(r.content)['aaData']]


def semshift(search_term):
    r = requests.get(
        f'https://csd.clld.org/parameters?sEcho=9&iColumns=4&sColumns=more%2Cname%2Csemantic_domain%2Cpart_of_speech&sSearch_1={search_term}&bRegex_1=false&bSearchable_1=true',
        headers={'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'})

    meanings = []
    try:
        ids = [html.fromstring(item[1]).attrib['href'].split('/')[-1] for item in json.loads(r.content)['aaData']]
        if len(ids) == 0:
            return []

        urls = [f'https://csd.clld.org/values?parameter={id}&sEcho=1&iColumns=6&sColumns=language%2Cname%2Cphonetic%2Cdescription%2Ccomment%2Csources' for id in ids]
        results = multi_request(urls,
                                headers={'accept': 'application/json',
                                         'x-requested-with': 'XMLHttpRequest'})

        for result in results:
            meanings += [item[-3] for item in json.loads(result.content)['aaData']]
    except json.decoder.JSONDecodeError:
        pass
    return list(set(meanings))