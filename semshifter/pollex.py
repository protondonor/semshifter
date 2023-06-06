import requests
from lxml import html

from helper import french

def semshift(search_term, include_french=False):
    try:
        r = requests.get(f'https://pollex.eva.mpg.de/search/?query=%5Cb{search_term}%5Cb&field=protoform', verify=False)
        tree = html.fromstring(r.content)
        meanings = []
        for elem in tree.xpath('/html/body/div/div[3]/table/tr/td/a'):
            r2 = requests.get(f"https://pollex.eva.mpg.de{elem.attrib['href']}", verify=False)
            tree2 = html.fromstring(r2.content)
            for entry in tree2.xpath('//*[@id="content"]/table[2]/tr/td[3]/text()'):
                if len(entry.strip()) > 0 and (include_french or not french(entry.strip())):
                    meanings.append(entry.strip())
        return meanings
    except ConnectionError:
        return []


def reverse(search_term, include_french=False):
    try:
        r = requests.get(f'https://pollex.eva.mpg.de/search/?query=%5Cb{search_term}%5Cb&field=entry', verify=False)
        tree = html.fromstring(r.content)
        meanings = []
        urls = set([f"https://pollex.eva.mpg.de{elem.attrib['href']}"
                    for elem in tree.xpath("/html/body/div/div[3]/table/tr/td[2]/a")])
        for url in urls:
            r2 = requests.get(url, verify=False)
            tree2 = html.fromstring(r2.content)
            try:
                entry = tree2.xpath('//*[@id="content"]/table[1]/tr[1]/td/text()')[0]
                if len(entry.strip()) > 0 and (include_french or not french(entry.strip())):
                    meanings.append(entry.strip())
            except IndexError:
                pass
        return meanings
    except ConnectionError:
        return []
