import csd, pollex, prototai, clics, stedt, datsemshift
from helper import clean_shift
import asyncio

dss = datsemshift.DatSemShift()


async def semshift(search_term, dictionaries=None, trace=False):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'prototai', 'clics', 'stedt', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        meanings['csd'] = clean_shift(await csd.semshift(search_term))
    if 'pollex' in dictionaries:
        meanings['pollex'] = clean_shift(pollex.semshift(search_term))
    if 'stedt' in dictionaries:
        meanings['stedt'] = clean_shift(await stedt.semshift(search_term))
    if 'clics' in dictionaries:
        meanings['clics'] = clean_shift(await clics.semshift(search_term))
    if 'dss' in dictionaries:
        meanings['dss'] = clean_shift(await dss.semshift(search_term))
    if 'prototai' in dictionaries:
        meanings['prototai']= clean_shift(await prototai.semshift(search_term))
    if trace:
        return meanings

    return {x for v in meanings.values() for x in v}


def reverse(search_term, dictionaries=None, trace=False):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'stedt', 'clics', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        meanings['csd'] = clean_shift(csd.reverse(search_term))
    if 'pollex' in dictionaries:
        meanings['pollex'] = clean_shift(pollex.reverse(search_term))
    if 'stedt' in dictionaries:
        meanings['stedt'] = clean_shift(stedt.reverse(search_term))
    if 'clics' in dictionaries:
        meanings['clics'] = clean_shift(clics.reverse(search_term))
    if 'dss' in dictionaries:
        meanings['dss'] = clean_shift(dss.reverse(search_term))
    if trace:
        return meanings

    return {x for v in meanings.values() for x in v}
