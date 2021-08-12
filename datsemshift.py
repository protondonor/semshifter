from helper import multi_request
from urllib.parse import quote
import requests
from lxml import html


class DatSemShift:
    cached_request = None
    source_phrases = []
    target_phrases = []

    def populate_sources(self):
        if self.cached_request is None:
            r = requests.get("http://datsemshift.ru/search")
            self.cached_request = html.fromstring(r.content)
        self.source_phrases = self.cached_request.xpath('//*[@id="source"]/option/text()')

    def populate_targets(self):
        if self.cached_request is None:
            r = requests.get("http://datsemshift.ru/search")
            self.cached_request = html.fromstring(r.content)
        self.target_phrases = self.cached_request.xpath('//*[@id="target"]/option/text()')

    async def semshift(self, search_term):
        if len(self.source_phrases) == 0:
            self.populate_sources()
        urls = [f'http://datsemshift.ru/search?source={quote(source_phrase)}'
                for source_phrase in self.source_phrases if search_term in source_phrase]

        results = await multi_request(urls)

        meanings = [item for sublist in
                    [html.fromstring(r.content).xpath('/html/body/main/div/table/tr/td[5]/text()') for r in results]
                    for item in sublist if item != 'Meaning 2']

        return meanings

    async def reverse(self, search_term):
        if len(self.target_phrases) == 0:
            self.populate_targets()
        urls = [f'http://datsemshift.ru/search?target={quote(input)}'
                for input in self.target_phrases if search_term in input]

        results = await multi_request(urls)

        meanings = [item for sublist in
                    [html.fromstring(r.content).xpath('/html/body/main/div/table/tr/td[3]/text()') for r in results]
                    for item in sublist if item != 'Meaning 1']

        return meanings
