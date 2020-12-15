import requests
from lxml import html


def semshift(search_term):
    r = requests.get(f'https://pollex.shh.mpg.de/search/?query={search_term}&field=protoform')
    tree = html.fromstring(r.content)
    meanings = []
    for elem in tree.xpath('/html/body/div/div[3]/table/tr/td/a'):
        r2 = requests.get(f"https://pollex.shh.mpg.de{elem.attrib['href']}")
        tree2 = html.fromstring(r2.content)
        for entry in tree2.xpath('//*[@id="content"]/table[2]/tr/td[3]/text()'):
            if len(entry.strip()) > 0:
                meanings.append(entry.strip())
    return meanings


def reverse(search_term):
    r = requests.get(f'https://pollex.shh.mpg.de/search/?query={search_term}&field=entry')
    tree = html.fromstring(r.content)
    meanings = []
    urls = set([f"https://pollex.shh.mpg.de{elem.attrib['href']}"
                for elem in tree.xpath("/html/body/div/div[3]/table/tr/td[2]/a")])
    for url in urls:
        r2 = requests.get(url)
        tree2 = html.fromstring(r2.content)
        try:
            entry = tree2.xpath('//*[@id="content"]/table[1]/tr[1]/td/text()')[0]
            if len(entry.strip()) > 0:
                meanings.append(entry.strip())
        except IndexError:
            pass
    return meanings
