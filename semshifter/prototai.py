import requests
from lxml import html

from semshifter.helper import remove_suffix


def semshift(search_term):
    payload = {
        'process': '..%2Fproto%2Fhtm.pl',
        'query': search_term,
        'matchWord': 'on',
        'matchHead': 'on',
        'matchTail': 'on',
        'showLi': 'on',
        'showLuo': 'on',
        'showBrown': 'on',
        'showJonsson': 'on',
        'allowLi': 'on',
        'allowLuo': 'on',
        'allowBrown': 'on',
        'allowJonsson': 'on',
        'showNoThai': 'on',
        'sortkey': 'thai'
    }

    r = requests.post('http://sealang.net/crcl/proto/htm.pl', data=payload)
    tree = html.fromstring(r.content.decode('utf-8', 'ignore'))
    return [remove_suffix(elem.strip('"'), " (as is)") for elem in
            [elem.strip() for elem in tree.xpath('/html/body/htm/font/text()')]
            if len(elem) > 0 and elem[0] == elem[-1] and elem[0] == '"']
