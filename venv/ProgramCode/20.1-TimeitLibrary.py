#Use timeit to compare the runtime of map(), for loops, and list comprehensions:
import random
import timeit

TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]

def get_price(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price, txns))

def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices

print(timeit.timeit(get_prices_with_map, number=100))
#O/P: 1.6269217
print(timeit.timeit(get_prices_with_comprehension, number=100))
#O/P: 2.0257826
print(timeit.timeit(get_prices_with_loop, number=100))
#O/P: 2.5884796