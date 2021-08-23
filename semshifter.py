from requests_cache import install_cache

import clics
import csd
import datsemshift
import pollex
import prototai
import stedt
from helper import clean_shift

dss = datsemshift.DatSemShift()
install_cache(cache_name='semshift', backend='sqlite', expire_after=604800)


def semshift(search_term, dictionaries=None, trace=False):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'prototai', 'clics', 'stedt', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        print("starting csd")
        meanings['csd'] = clean_shift(csd.semshift(search_term))
        print("exiting csd")
    if 'pollex' in dictionaries:
        print("starting pollex")
        meanings['pollex'] = clean_shift(pollex.semshift(search_term))
        print("exiting pollex")
    if 'stedt' in dictionaries:
        print("starting stedt")
        meanings['stedt'] = clean_shift(stedt.semshift(search_term))
        print("exiting stedt")
    if 'clics' in dictionaries:
        print("starting clics")
        meanings['clics'] = clean_shift(clics.semshift(search_term))
        print("exiting clics")
    if 'dss' in dictionaries:
        print("starting dss")
        meanings['dss'] = clean_shift(dss.semshift(search_term))
        print("exiting dss")
    if 'prototai' in dictionaries:
        print("starting prototai")
        meanings['prototai'] = clean_shift(prototai.semshift(search_term))
        print("exiting prototai")
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
