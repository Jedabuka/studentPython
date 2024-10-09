import unittest
import module_12_4_logi
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = True

    def test_walk(self):
        try:
            runner = module_12_4_logi.Runner('Вася', -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 100)

        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner1 = module_12_4_logi.Runner(['Илья'], 5)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                runner1.run()
            self.assertEqual(runner1.distance, 50)

        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        runner2 = module_12_4_logi.Runner('Макс')
        runner3 = module_12_4_logi.Runner('Ден')
        for i in range(10):
            runner2.run()
            runner3.walk()
        self.assertNotEqual(runner2.distance, runner3.distance)


if __name__ == '__main__':
    unittest.main()


