import unittest
import module_12_2


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = module_12_2.Runner('Усэйн', speed=10)
        self.runner2 = module_12_2.Runner('Андрей', speed=9)
        self.runner3 = module_12_2.Runner('Ник', speed=3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament(self):
        tour1 = module_12_2.Tournament(90, self.runner1, self.runner3)
        res = tour1.start()
        self.all_result[1] = res
        runners = list(res.values())
        self.assertTrue(runners[-1] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament1(self):
        tour2 = module_12_2.Tournament(90, self.runner2, self.runner3)
        res = tour2.start()
        self.all_result[2] = res
        runners = list(res.values())
        self.assertTrue(runners[-1] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament2(self):
        tour3 = module_12_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = tour3.start()
        self.all_result[3] = res
        runners = list(res.values())
        self.assertTrue(runners[-1] == self.runner3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result.values():
            print({place: str(runner) for place, runner in result.items()})


if __name__ == '__main__':
    unittest.main()
