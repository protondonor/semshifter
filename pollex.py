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
    for elem in tree.xpath("/html/body/div/div[3]/table/tr/td[2]/a"):
        r2 = requests.get(f"https://pollex.shh.mpg.de{elem.attrib['href']}")
        tree2 = html.fromstring(r2.content)
        for entry in tree2.xpath('//*[@id="content"]/table[2]/tr/td[3]/text()'):
            if len(entry.strip()) > 0:
                meanings.append(entry.strip())
    return meanings
