import json
import unittest
from unittest.mock import patch, Mock

from clics import semshift


class TestClics(unittest.TestCase):
    clics_html = Mock()
    clics_html.content = """<html>
<body>
<thead>
<tr>
<th style="text-align: right">Links</th>
<th>Concept</th>
</tr>
</thead>
<tbody>
<tr>
<td class="right">98</td>
<td><a class="Edge" href="https://clics.clld.org/edges/2-646" title="ASH">ASH</a></td>
</tr>
<tr>
<td class="right">27</td>
<td><a class="Edge" href="https://clics.clld.org/edges/2-1228" title="EARTH (SOIL)">EARTH (SOIL)</a></td>
</tr>
<tr>
<td class="right">24</td>
<td><a class="Edge" href="https://clics.clld.org/edges/2-249" title="FOG">FOG</a></td>
</tr>
<tr>
<td class="right">23</td>
<td><a class="Edge" href="https://clics.clld.org/edges/2-778" title="SMOKE (EXHAUST)">SMOKE (EXHAUST)</a></td>
</tr>
</tbody>
</body>
</html>
"""
    clics_json = json.dumps({
        'aaData': [
            [
                'more',
                '<a href="http://zombo.com/1">closed</a>',
                'some', 'other', 'stuff', 'idk'
            ],
            [
                'more',
                '<a href="http://zombo.com/2">close (eyes)</a>',
                'some', 'other', 'stuff', 'idk'
            ]
        ]
    })

    def test_semshift(self):
        with patch('requests.get') as mock_r, patch('clics.multi_request') as mock_multi_r:
            mock_r.return_value.content = self.clics_json
            mock_multi_r.return_value = [self.clics_html]

            meanings = semshift("close")
            self.assertSetEqual(set(meanings), {"ASH", "EARTH (SOIL)", "FOG", "SMOKE (EXHAUST)"})

            mock_r.assert_called_once_with(
                f'https://clics.clld.org/parameters?sEcho=9&iColumns=7&sColumns=%23%2Cname%2C%23%2C'
                f'count_varieties%2Ccount_colexifications%2Cinfomap%2Csubgraph&iDisplayStart=0&'
                f'iDisplayLength=100&mDataProp_1=1&sSearch_1=close',
                headers={'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'})

            mock_multi_r.assert_called_once_with([
                "http://zombo.com/1",
                "http://zombo.com/2"
            ])


if __name__ == '__main__':
    unittest.main()
