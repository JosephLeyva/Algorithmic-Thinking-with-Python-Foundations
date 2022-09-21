'''
THE CHANGE-MAKING PROBLEM
--------------------------------- 
Find the minimum number of coins from a set of denominations that add up to a given amount of money.
'''
DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]


def make_change(target_amount):
    # Store the target on remainder (we will subtract each time we find a coin)
    remainder = target_amount
    coins = 0  # Initialize number of coins
    coin_values = []  # Create a list where we are going to store the coin values

    while remainder != 0:  # Check if there is no remainder left
        i = 0

        # Here we check if the value is not greater than the remainder, if so, move to the next coin
        while DENOMINATIONS[i] > remainder:
            i += 1
        # Here we are on the position where the current coin is less than the remainder
        coins += 1
        accumulated = DENOMINATIONS[i]
        coin_values.append(accumulated)  # We append the coin value on the list
        remainder -= accumulated  # We subtract the value of the coin from the remainder

    return coins, coin_values


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
