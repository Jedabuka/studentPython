import unittest
import module_12_1


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        runner = module_12_1.Runner('Миша')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        runner1 = module_12_1.Runner('Саня')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        runner2 = module_12_1.Runner('Макс')
        runner3 = module_12_1.Runner('Ден')
        for i in range(10):
            runner2.run()
            runner3.walk()
        self.assertNotEqual(runner2.distance, runner3.distance)


if __name__ == '__main__':
    unittest.main()
