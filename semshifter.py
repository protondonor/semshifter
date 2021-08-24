from requests_cache import install_cache

import clics
import csd
import datsemshift
import pollex
import prototai
import stedt
import logging
from helper import clean_shift

dss = datsemshift.DatSemShift()
install_cache(cache_name='semshift', backend='sqlite', expire_after=604800)


def semshift(search_term, dictionaries=None, trace=False):
    logging.log(logging.INFO, f'shifting {search_term}')
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'prototai', 'clics', 'stedt', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        logging.log(logging.INFO, "starting csd")
        meanings['csd'] = clean_shift(csd.semshift(search_term))
        logging.log(logging.INFO, "exiting csd")
    if 'pollex' in dictionaries:
        logging.log(logging.INFO, "starting pollex")
        meanings['pollex'] = clean_shift(pollex.semshift(search_term))
        logging.log(logging.INFO, "exiting pollex")
    if 'stedt' in dictionaries:
        logging.log(logging.INFO, "starting stedt")
        meanings['stedt'] = clean_shift(stedt.semshift(search_term))
        logging.log(logging.INFO, "exiting stedt")
    if 'clics' in dictionaries:
        logging.log(logging.INFO, "starting clics")
        meanings['clics'] = clean_shift(clics.semshift(search_term))
        logging.log(logging.INFO, "exiting clics")
    if 'dss' in dictionaries:
        logging.log(logging.INFO, "starting dss")
        meanings['dss'] = clean_shift(dss.semshift(search_term))
        logging.log(logging.INFO, "exiting dss")
    if 'prototai' in dictionaries:
        logging.log(logging.INFO, "starting prototai")
        meanings['prototai'] = clean_shift(prototai.semshift(search_term))
        logging.log(logging.INFO, "exiting prototai")
    if trace:
        return meanings

    return {x for v in meanings.values() for x in v}


def reverse(search_term, dictionaries=None, trace=False):
    if dictionaries is None:
        dictionaries = ['csd', 'pollex', 'stedt', 'clics', 'dss']
    meanings = {}
    if 'csd' in dictionaries:
        logging.log(logging.INFO, "starting csd")
        meanings['csd'] = clean_shift(csd.reverse(search_term))
        logging.log(logging.INFO, "exiting csd")
    if 'pollex' in dictionaries:
        logging.log(logging.INFO, "starting pollex")
        meanings['pollex'] = clean_shift(pollex.reverse(search_term))
        logging.log(logging.INFO, "exiting pollex")
    if 'stedt' in dictionaries:
        logging.log(logging.INFO, "starting stedt")
        meanings['stedt'] = clean_shift(stedt.reverse(search_term))
        logging.log(logging.INFO, "exiting stedt")
    if 'clics' in dictionaries:
        logging.log(logging.INFO, "starting clics")
        meanings['clics'] = clean_shift(clics.reverse(search_term))
        logging.log(logging.INFO, "exiting clics")
    if 'dss' in dictionaries:
        logging.log(logging.INFO, "starting dss")
        meanings['dss'] = clean_shift(dss.reverse(search_term))
        logging.log(logging.INFO, "exiting dss")
    if trace:
        return meanings

    return {x for v in meanings.values() for x in v}
