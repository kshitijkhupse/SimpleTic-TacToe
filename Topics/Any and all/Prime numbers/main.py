prime_numbers = [x for x in range(2, 1001) if x > 1 and all(x % i != 0 for i in range(2, x-1))]

