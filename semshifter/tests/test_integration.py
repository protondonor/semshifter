import unittest
import clics
import csd
import datsemshift
import pollex
import prototai
import stedt


class Integration(unittest.TestCase):
    def test_clics(self):
        dust = clics.semshift("dust")
        self.assertSetEqual(set(dust),
                            {'ASH', 'EARTH (SOIL)', 'FOG', 'SMOKE (EXHAUST)', 'LAND', 'SAND', 'FLOUR', 'CLAY', 'MUD',
                             'CLOUD'})

    def test_csd(self):
        grape = csd.semshift("grape")
        self.assertSetEqual(set(grape),
                            {'raspberry', 'grapes', 'strawberry', 'mayhaws', 'strawberries', '[berry, grape]',
                             'berry, fruit', 'grape', 'berry, berries', 'chokecherry', 'berry', 'bullberry',
                             'blackberry'}
                            )

    def test_pollex(self):
        chisel = pollex.semshift("chisel")
        self.assertSetEqual(set(chisel), {'Tattooing stick bearing bones or needles', 'Tattooing chisel',
                                          "Tattooer's serrated chisel of bird-bone"})

    def test_prototai(self):
        tiger = prototai.semshift("tiger")
        self.assertSetEqual(set(tiger), {'tiger'})

    def test_stedt(self):
        scorpion = stedt.semshift("scorpion")
        self.assertSetEqual(set(scorpion),
                            {'scorpion', 'scorpion [m-bug]', 'shrimp', 'scorpion / crab / shrimp', 'shrimp / scorpion',
                             'crab, crawfish'})

    def test_datsemshift(self):
        dss = datsemshift.DatSemShift()
        closed = dss.semshift("closed")
        self.assertSetEqual(set(closed), {'dark (adj.)', 'strong (of liquid or smell)', 'cloudy'})


if __name__ == '__main__':
    unittest.main()
