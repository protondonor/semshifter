import csd, pollex, prototai, clics, stedt, datsemshift
from helper import clean_shift

dss = datsemshift.DatSemShift()


def semshift(search_term, dictionaries=None, trace=False):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'prototai', 'clics', 'stedt', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        meanings['csd'] = clean_shift(map(str.lower, csd.semshift(search_term)))
    if 'pollex' in dictionaries:
        meanings['pollex'] = clean_shift(map(str.lower, pollex.semshift(search_term)))
    if 'stedt' in dictionaries:
        meanings['prototai'] = clean_shift(map(str.lower, stedt.semshift(search_term)))
    if 'clics' in dictionaries:
        meanings['clics'] = clean_shift(map(str.lower, clics.semshift(search_term)))
    if 'dss' in dictionaries:
        meanings['dss'] = clean_shift(map(str.lower, dss.semshift(search_term)))
    if 'prototai' in dictionaries:
        meanings['prototai']= clean_shift(map(str.lower, prototai.semshift(search_term)))
    if trace:
        return meanings

    return {x for v in meanings.values() for x in v}


def reverse(search_term, dictionaries=None):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'stedt', 'clics', 'dss']
    meanings = []
    if 'csd' in dictionaries:
        meanings += csd.reverse(search_term)
    if 'pollex' in dictionaries:
        meanings += pollex.reverse(search_term)
    if 'stedt' in dictionaries:
        meanings += stedt.reverse(search_term)
    if 'clics' in dictionaries:
        meanings += clics.reverse(search_term)
    if 'dss' in dictionaries:
        meanings += dss.reverse(search_term)

    return clean_shift(set(map(str.lower, meanings)))
