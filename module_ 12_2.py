import unittest
from pprint import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    def test_tournament(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        res = tour1.start()
        self.all_result[1] = res
        runners = list(res.values())
        self.assertTrue(runners[-1] == self.runner3)

    def test_tournament1(self):
        tour2 = Tournament(90, self.runner1, self.runner3)
        res = tour2.start()
        self.all_result[2] = res
        runners = list(res.values())
        self.assertTrue(runners[-1] == self.runner3)

    def test_tournament2(self):
        tour3 = Tournament(90, self.runner1, self.runner2, self.runner3)
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











