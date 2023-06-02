import unittest


class TestStedt(unittest.TestCase):
    def test_trim(self):
        from stedt import trim

        crab = '\n#2304 PTB *d-k(y)aːy CRAB'
        self.assertEqual(trim(crab), 'crab')

        draw_water = '\n#2296 PTB *kaː(p/m) DRAW (water) / SCOOP (water) / CONCAVE'
        self.assertEqual(trim(draw_water), 'draw (water) / scoop (water) / concave')

        sprinkle = '\n#5694 PTB *m/s-prat ⪤ *pran SPRINKLE / SPRAY'
        self.assertEqual(trim(sprinkle), 'sprinkle / spray')

        wallow = '\n#5064 PKC *looŋ-I, loŋʔ-II WALLOW / ROLL ABOUT '
        self.assertEqual(trim(wallow), 'wallow / roll about')
