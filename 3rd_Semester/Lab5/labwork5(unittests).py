import timeit
import matplotlib.pyplot as plt
import unittest

def memoize(func):
    cache = {}
    
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

def fact_recursive(value):
    if value == 0 or value == 1:
        return 1
    return value * fact_recursive(value - 1)

def fact_iterative(value):
    rslt = 1
    for current in range(1, value + 1):
        rslt *= current
    return rslt

@memoize
def fact_recursive_memo(value):
    if value == 0 or value == 1:
        return 1
    return value * fact_recursive_memo(value - 1)  

@memoize
def fact_iterative_memo(value):
    rslt = 1
    for current in range(1, value + 1):
        rslt *= current
    return rslt

def benchmark(func, data, number=10000, repeat=5):
    ttl = 0
    for n in data:
        tms = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
        ttl += min(tms)
    return ttl / len(data)

def main():
    tst_data = list(range(10, 150, 10))
    rslt_recursive = []
    rslt_iterative = []
    rslt_recursive_memo = []
    rslt_iterative_memo = []

    fact_recursive_memo.__closure__[0].cell_contents.clear()
    fact_iterative_memo.__closure__[0].cell_contents.clear()
    
    for n in tst_data:
        rslt_recursive.append(benchmark(fact_recursive, [n]))
        rslt_iterative.append(benchmark(fact_iterative, [n]))
        rslt_recursive_memo.append(benchmark(fact_recursive_memo, [n]))
        rslt_iterative_memo.append(benchmark(fact_iterative_memo, [n]))

    plt.plot(tst_data, rslt_recursive, label="Рекурсивный")
    plt.plot(tst_data, rslt_iterative, label="Итеративный")
    plt.plot(tst_data, rslt_recursive_memo, label="Рекурсивный с мемоизацией")
    plt.plot(tst_data, rslt_iterative_memo, label="Итеративный с мемоизацией")
    
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение методов вычисления факториала")
    plt.legend()
    plt.grid(True)
    plt.show()

class TestFactorialFunctions(unittest.TestCase):
    
    def test_fact_recursive_basic_values(self):
        """проверка рекурсивной функции на базовых значениях"""
        self.assertEqual(fact_recursive(0), 1)
        self.assertEqual(fact_recursive(1), 1)
        self.assertEqual(fact_recursive(5), 120)
        self.assertEqual(fact_recursive(10), 3628800)
    
    def test_fact_iterative_basic_values(self):
        """проверка итеративной функции на базовых значениях"""
        self.assertEqual(fact_iterative(0), 1)
        self.assertEqual(fact_iterative(1), 1)
        self.assertEqual(fact_iterative(5), 120)
        self.assertEqual(fact_iterative(10), 3628800)
    
    def test_consistency_between_methods(self):
        """проверка согласованности результатов для разных методов"""
        test_values = [0, 1, 5, 10, 15]
        for n in test_values:
            with self.subTest(n=n):
                recursive_result = fact_recursive(n)
                iterative_result = fact_iterative(n)
                self.assertEqual(recursive_result, iterative_result,
                               f"расхождение при n={n}: рекурсия={recursive_result}, итерация={iterative_result}")
    
    def test_memoized_functions_correctness(self):
        """проверка корректности мемоизированных функций"""
        test_values = [0, 1, 5, 10]
        for n in test_values:
            with self.subTest(n=n):
                # Очищаем кэш перед каждым тестом
                fact_recursive_memo.__closure__[0].cell_contents.clear()
                fact_iterative_memo.__closure__[0].cell_contents.clear()
                
                original_result = fact_recursive(n)
                memoized_result = fact_recursive_memo(n)
                self.assertEqual(original_result, memoized_result)
    
    def test_memoization_cache_works(self):
        """проверка работы кэширования в мемоизации"""
        #очищаем кэш
        fact_recursive_memo.__closure__[0].cell_contents.clear()
        
        #первый вызов должен вычислить, второй взять значение из кэша
        first_call = fact_recursive_memo(10)
        second_call = fact_recursive_memo(10)
        
        self.assertEqual(first_call, second_call)
        #проверяем что значение есть в кэше
        cache = fact_recursive_memo.__closure__[0].cell_contents
        self.assertIn(10, cache)
        self.assertEqual(cache[10], 3628800)
    
    def test_edge_cases_and_validation(self):
        """проверка граничных случаев и валидации"""
        #должны корректно обрабатывать 0 и 1
        self.assertEqual(fact_recursive(0), 1)
        self.assertEqual(fact_iterative(0), 1)
        
        #отрицательные числа должны вызывать ошибку
        with self.assertRaises(RecursionError):
            fact_recursive(-1)
    
    def test_memoize_decorator_independence(self):
        """проверка что декоратор создает независимые кэши для разных функций"""
        @memoize
        def test_func1(x):
            return x * 2
        @memoize  
        def test_func2(x):
            return x * 3
        
        test_func1(5)
        test_func2(5)
        
        cache1 = test_func1.__closure__[0].cell_contents
        cache2 = test_func2.__closure__[0].cell_contents
        
        self.assertIsNot(cache1, cache2)
        self.assertEqual(cache1[5], 10)
        self.assertEqual(cache2[5], 15)
    
    def test_large_values_performance(self):
        """проверка работы с большими значениями"""
        #итеративная функция должна работать с большими n
        large_n = 100
        result = fact_iterative(large_n)
        self.assertTrue(result > 0)
    
    def test_memoized_recursive_consistency(self):
        """проверка согласованности мемоизированной рекурсии с оригиналом"""
        test_values = [1, 2, 3, 4, 5, 6, 7, 8]
        for n in test_values:
            with self.subTest(n=n):
                #очищаем кэш перед каждым тестом
                fact_recursive_memo.__closure__[0].cell_contents.clear()
                
                original = fact_recursive(n)
                memoized = fact_recursive_memo(n)
                self.assertEqual(original, memoized)
    
    def test_benchmark_data_structure(self):
        """проверка структуры данных для бенчмарка"""
        tst_data = list(range(10, 150, 10))
        
        #проверяем что данные для тестирования корректны
        self.assertIsInstance(tst_data, list)
        self.assertTrue(len(tst_data) > 0)
        self.assertTrue(all(isinstance(x, int) for x in tst_data))
        self.assertTrue(all(x >= 0 for x in tst_data))

if __name__ == "__main__":
    unittest.main()