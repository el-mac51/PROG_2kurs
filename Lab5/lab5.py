import timeit
import matplotlib.pyplot as plt

#декоратор для мемоизации
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

#применяем декоратор
@memoize
def fact_recursive_memo(value):
    if value == 0 or value == 1:
        return 1
    return value * fact_recursive_memo(value - 1)  #рекурсивные вызовы тоже идут через декоратор

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

if __name__ == "__main__":
    main()