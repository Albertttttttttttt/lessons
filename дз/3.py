import multiprocessing

def sum_even_numbers(start, end):
    total = 0
    for i in range(start, end):
        if i % 2 == 0:
            total += i
    return total

def sum_odd_numbers(start, end):
    total = 0
    for i in range(start, end):
        if i % 2 != 0:
            total += i
    return total

if __name__ == '__main__':
    start, end = 1, 1000001
    with multiprocessing.Pool(processes=2) as pool:
        result1 = pool.apply_async(sum_even_numbers, args=(start, end))
        result2 = pool.apply_async(sum_odd_numbers, args=(start, end))
        print(f"Sum of even numbers from {start} to {end}: {result1.get()}")
        print(f"Sum of odd numbers from {start} to {end}: {result2.get()}")