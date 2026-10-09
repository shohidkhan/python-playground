# loop 


fruits = ["apple", "banana", "cherry"]
for fruit  in fruits:
    print(fruit)


product_prices=[1, 2, 3, 4, 5]

cent_prices=[]

for price in product_prices:
    cent_price=price*100
    cent_prices.append(cent_price)



float_prices=[1.5, 2.5, 3.5, 4.5, 5.5]

int_prices=[ int(price*2) for price in float_prices]


print(int_prices)