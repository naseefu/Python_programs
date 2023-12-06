coins = list(map(int,input('enter the target').split()))
target = int(input('enter the target'))

dp = [int('inf')] * (target + 1)
dp[0] = 0

for i in range(1,target+1):
    for coin in coins:
        if i-coin>=0:
            dp[i] = min(dp[i],dp[i-coin]+1)
print(dp[target])
