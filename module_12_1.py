import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):

    def test_walk(self):
        runner = Runner('Миша')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner1 = Runner('Саня')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    def test_challenge(self):
        runner2 = Runner('Макс')
        runner3 = Runner('Ден')
        for i in range(10):
            runner2.run()
            runner3.walk()
        self.assertNotEqual(runner2.distance, runner3.distance)


if __name__ == '__main__':
    unittest.main()
