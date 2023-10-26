
def coinChange(coins, amount):
    # Función recursiva para calcular la cantidad mínima de monedas
    def helper(coins, amount, memo):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        min_coins = float('inf')
        for coin in coins:
            res = helper(coins, amount - coin, memo)
            if res >= 0:
                min_coins = min(min_coins, res + 1)

        memo[amount] = -1 if min_coins == float('inf') else min_coins
        return memo[amount]

    return helper(coins, amount, {})


result = coinChange([1,2,5], 11)
print(result)
