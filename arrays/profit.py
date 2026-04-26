def max_profit(arr):
    min_price = float('inf')
    max_profit = 0
    for price in arr:
        if min_price>price:
            min_price = price
        else:
            profit = price-min_price
            if profit>max_profit:
                max_profit = profit
    return max_profit

ls = list(map(int,input().split(" ")));
print(max_profit(ls))