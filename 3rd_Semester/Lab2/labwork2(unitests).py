import unittest
from labwork1 import sums #первый вариант подключения функции

class TestSums(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(sums([2, 7, 11, 15], 9), [0, 1])
        
    def test_example2(self):
        self.assertEqual(sums([3, 2, 4], 6), [1, 2])
        
    def test_example3(self):
        self.assertEqual(sums([3, 3], 6), [0, 1])
        
    def test_no_solution(self):
        self.assertEqual(sums([1, 4, 9], 37), None) #None потому что с пустыми скобками выдает ошибку: None!=[]
        
    def test_negative_numbers(self):
        self.assertEqual(sums([-1, -3, -5, -9], -8), [1, 2])
        
    def test_same_number_twice(self):
        self.assertEqual(sums([5, 5, 14], 10), [0, 1])

if __name__ == "__main__":
    unittest.main()
