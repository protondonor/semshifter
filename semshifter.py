import csd, pollex, prototai, clics, stedt, datsemshift
from helper import clean_shift

dss = datsemshift.DatSemShift()

def semshift(search_term):
    meanings = csd.semshift(search_term) + pollex.semshift(search_term) + prototai.semshift(search_term) + \
               clics.semshift(search_term) + stedt.semshift(search_term) + dss.semshift(search_term)
    return clean_shift(set(map(str.lower, meanings)))


def reverse(search_term, dictionaries=None):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'stedt', 'clics']
    meanings = []
    if 'csd' in dictionaries:
        meanings += csd.reverse(search_term)
    if 'pollex' in dictionaries:
        meanings += pollex.reverse(search_term)
    if 'stedt' in dictionaries:
        meanings += stedt.reverse(search_term)
    if 'clics' in dictionaries:
        meanings += clics.reverse(search_term)

    return clean_shift(set(map(str.lower, meanings)))