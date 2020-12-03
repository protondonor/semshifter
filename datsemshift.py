from helper import multi_request
from urllib.parse import quote
import requests
from lxml import html


class DatSemShift:
    dss_input_phrases = []

    def populate_dss_input_phrases(self):
        r = requests.get("http://datsemshift.ru/search")
        tree = html.fromstring(r.content)
        self.dss_input_phrases = tree.xpath('//*[@id="source"]/option/text()')

    def semshift(self, search_term):
        if len(self.dss_input_phrases) == 0:
            self.populate_dss_input_phrases()
        urls = [f'http://datsemshift.ru/search?source={quote(input)}'
                for input in self.dss_input_phrases if search_term in input]

        results = multi_request(urls)

        meanings = [item for sublist in
                    [html.fromstring(r.content).xpath('/html/body/main/div/table/tr/td[5]/text()') for r in results]
                    for item in sublist if item != 'Meaning 2']

        return meanings
