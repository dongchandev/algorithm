import sys

n = int(sys.stdin.readline().rstrip())

if n < 4:
    if n == 2:
        print("CY")
    else:
        print("SK")
    quit()

dp = [0] * (n + 1)
dp[1], dp[3], dp[4] = "SK", "SK", "SK"
dp[2] = "CY"

for i in range(5, n + 1):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY" or dp[i - 4] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"
print(dp[-1])
