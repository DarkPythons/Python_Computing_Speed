"""
Код 10 способа вычисления чисел фибоначчи.
Использование подхода к вычислению чисел фибоначчи из динамического программирования
"""

import time
from fib_settings import MAX_FIB_NUMBER

def main():

    start_time = time.time()

    results_list = [0, 1] + [None] * (MAX_FIB_NUMBER-1)

    for one_index in range(2, MAX_FIB_NUMBER+1):
        # Берем предудещее значение по индексу, еще более дальнее значение по индексу и складываем 
        # их
        results_list[one_index] = results_list[one_index-1] + results_list[one_index-2]

    end_time = time.time()

    print(f"Все вычисления заняли: {end_time - start_time} секунд")
    print(results_list)

if __name__ == "__main__":
    main()

"""
Результат:
Все вычисления заняли: 0.0 секунд
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 
17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 
5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
"""