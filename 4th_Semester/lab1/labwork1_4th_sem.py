
import functools
import itertools
from typing import Generator, List


class FibonacciIterator:
    """
    Итератор для генерации чисел Фибоначчи
    
    Реализует протокол итератора через методы __iter__ и __next__
    
    Args:
        count: Количество элементов для генерации
    """

    def __init__(self, count: int) -> None:
        self.count = count
        self.current = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> 'FibonacciIterator':
        return self

    def __next__(self) -> int:
        if self.current >= self.count:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return result


def fibonacci_generator(count: int) -> Generator[int, None, None]:
    """
    Генератор для получения чисел Фибоначчи
    
    Args:
        count: Количество элементов для генерации
        
    Yields:
        Следующее число Фибоначчи
    """
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def fib_elem_gen() -> Generator[int, None, None]:
    """
    Вспомогательный бесконечный генератор чисел Фибоначчи
    
    Yields:
        Следующее число Фибоначчи
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_coroutine() -> Generator[List[int], int, None]:
    """
    Сопрограмма для генерации списка чисел Фибоначчи
    
    Принимает через send() количество элементов и возвращает список
    Работает в бесконечном цикле, позволяя многократные запросы
    
    Yields:
        Список чисел Фибоначчи
        
    Receives:
        Количество элементов для генерации
    """
    result: List[int] = []
    
    while True:
        count = yield result
        
        if count is None or count <= 0:
            result = []
            continue
        
        result = list(itertools.islice(fib_elem_gen(), count))


def coroutine(func):
    """
    Декоратор для автоматического запуска сопрограммы
    
    Продвигает генератор до первого yield, чтобы он мог принимать send()
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return inner

#декоратор к сопрограмме
fibonacci_coroutine = coroutine(fibonacci_coroutine)