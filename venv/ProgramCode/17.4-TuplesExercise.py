"""
We can represent each block of stock as a 5-tuple with purchase date, purchase price, shares, ticker symbol and current price.

Develop a function that examines each block,
multiplies shares by purchase price and determines the total purchase price of the portfolio.

Develop a second function that examines each block,
multiplies shares by purchase price and shares by current price to determine the total amount gained or lost.

a. Compute Mean
b. Compute Standard Deviation
"""
#portfolio = (PurchaseDate, PurchasePrice, Shares, TickerSymbol, CurrentPrice
portfolio= [ ( "25-Jan-2001", 43.50, 25, 'CAT', 92.45 ),
( "25-Jan-2001", 42.80, 50, 'DD', 51.19 ),
( "25-Jan-2001", 42.10, 75, 'EK', 34.87 ),
( "25-Jan-2001", 37.58, 100, 'GM', 37.58 )
]