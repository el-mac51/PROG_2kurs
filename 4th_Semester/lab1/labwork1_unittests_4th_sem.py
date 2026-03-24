import unittest
from labwork1_4th_sem import FibonacciIterator, fibonacci_generator, fibonacci_coroutine

class TestFibonacciIterator(unittest.TestCase):
    def test_count(self):
        """Проверка количества элементов."""
        self.assertEqual(len(list(FibonacciIterator(5))), 5)
    
    def test_values(self):
        """Проверка значений последовательности."""
        self.assertEqual(list(FibonacciIterator(6)), [0, 1, 1, 2, 3, 5])
    
    def test_zero(self):
        """Проверка пустой последовательности."""
        self.assertEqual(list(FibonacciIterator(0)), [])

class TestFibonacciGenerator(unittest.TestCase):
    def test_count(self):
        """Проверка количества элементов."""
        self.assertEqual(len(list(fibonacci_generator(7))), 7)
    def test_values(self):
        """Проверка значений последовательности."""
        self.assertEqual(list(fibonacci_generator(8)), [0, 1, 1, 2, 3, 5, 8, 13])

class TestFibonacciCoroutine(unittest.TestCase):
    def test_multiple_requests(self):
        """Проверка многократных запросов к одной сопрограмме."""
        cor = fibonacci_coroutine()
        self.assertEqual(cor.send(3), [0, 1, 1])
        self.assertEqual(cor.send(5), [0, 1, 1, 2, 3])
        self.assertEqual(cor.send(1), [0])
    
    def test_zero(self):
        """Проверка запроса нуля элементов."""
        cor = fibonacci_coroutine()
        self.assertEqual(cor.send(0), [])

if __name__ == '__main__':
    unittest.main()