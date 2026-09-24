def calculate_discount(price, discount):
    '''
    calculates a discount on a product of original price
    price and discount discount%
    '''
    if (not ((isinstance(price, int) or
        isinstance(price, float)) and
        (isinstance(discount, int) or
        isinstance(discount, float)))):
        print("Price or Discount is not a number!!!")
        return 0
    else:
        return float(round(price * (discount / 100), 2))