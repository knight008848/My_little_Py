import unittest
import main_dom
import main_sax

sample_cd = \
    {'North America': 37, 'Asia': 51, 'Africa': 58, 'Europe': 46, 'South America': 14, 'Oceania': 28, 'Antarctica': 5}
sample_pd = \
    {'North America': 482993000, 'Asia': 3705025700, 'Africa': 784475000, 'Europe': 730074600, 'South America': 345780000, 'Oceania': 30401150, 'Antarctica': 0}


class TestDOM(unittest.TestCase):
    def test1(self):
        self.assertEqual(sample_cd, main_dom.get_continent('country.xml'))

    def test2(self):
        self.assertEqual(sample_pd, main_dom.get_population('country.xml'))


class TestSAX(unittest.TestCase):
    def test3(self):
        self.assertEqual(sample_cd, main_sax.get_continent('country.xml'))

    def test4(self):
        self.assertEqual(sample_pd, main_sax.get_population('country.xml'))

if __name__ == '__main__':
    unittest.main()
