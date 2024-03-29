import math
import re

import langid
import requests
from requests_html import AsyncHTMLSession
from requests_cache import CacheMixin

class CachedAsyncHTMLSession(CacheMixin, AsyncHTMLSession):
    """"Session with features of both CachedSession and AsyncHTMLSession"""


def multi_request(urls, headers=None):
    if len(urls) == 0:
        return []
    if headers is None:
        headers = {}
    try:
        session = CachedAsyncHTMLSession()

        scrape_fns = []
        for url in urls:
            async def get_site_content(url=url):
                return await session.get(url, headers=headers)

            scrape_fns.append(get_site_content)

        results = session.run(*scrape_fns)
        session.close()

        return results
    except RuntimeError as e:
        if 'event loop' in str(e):
            print(f'{str(e)}; falling back to synchronous requests')
            return [requests.post(url) for url in urls]


def first_numeric(datum):
    try:
        return int(next(x for x in datum.split(',') if x.isnumeric()))
    except StopIteration:
        return 0


def clean_shift(raw_output):
    cleaned_output = [word.strip('[ ]') for middle in map(str.lower, raw_output) for word in
                      re.split(r', or|,|\\|/|;|\.', re.sub(r'( \[|\().*([)\]])', '', middle).replace('?', '')) if
                      word.strip('[ ]')]
    return list(set(cleaned_output))


def remove_suffix(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string


def french(entry):
    lang, confidence = langid.classify(entry)
    return lang == 'fr' and math.fabs(confidence) > 50