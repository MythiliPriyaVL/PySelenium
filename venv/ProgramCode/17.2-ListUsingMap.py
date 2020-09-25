#Creating List using map() object
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = list(map(get_price_with_tax, txns))
#final_prices = [get_price_with_tax(i) for i in txns]  #using List Comprehension
print(final_prices)

#O/P: [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]