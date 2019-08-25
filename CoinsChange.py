def getWays(change, coins):
    quantity_coins=len(coins)
    table= [[0 for x in range(change+1)] for x in range(quantity_coins+1)] 
    
    for row in range(quantity_coins+1):
        table[row][0]=1
    
    for coin_position in range(1,quantity_coins+1):
        for current_change in range(change+1):
            current_coin=coins[coin_position-1]
            quantity_with_coin=table[coin_position][current_change-current_coin] if current_change-current_coin>=0 else 0
            quantity_without_coin=table[coin_position-1][current_change] if coin_position>=1 else 0
            table[coin_position][current_change]=quantity_with_coin+quantity_without_coin

    return table[-1][-1]






if __name__ == "__main__":

    coins=[1,3,5]
    change=8

    print(getWays(change,coins))