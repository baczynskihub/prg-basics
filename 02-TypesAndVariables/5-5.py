price=float(input("enter price:"))
discount=float(input("enter discount %:"))/100
discounted_prodcut_price=price*discount 
reduction=price-discounted_prodcut_price
print(f'price: {price}')
print(f'discount: {discount}')
print(f'price with discount: {discounted_prodcut_price}')
print(f'reduction: {reduction}')
            