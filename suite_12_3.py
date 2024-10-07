import unittest
import module_12_1_test
import module_12_2_test

go_test_suite = unittest.TestSuite()
go_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1_test.RunnerTest))
go_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_test.TournamentTest))

start_suite = unittest.TextTestRunner(verbosity=2)
start_suite.run(go_test_suite)

