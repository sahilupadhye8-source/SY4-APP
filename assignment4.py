def fibonacci(n,memo={}):
    if n in memo:
        return memo[n]

    if n<=1:
        return n
    memo[n]= fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]

n=int(input("enter the value of n:"))
print("fiboncci number =",fibonacci(n))

#tabulation
def fibonacci_tab(n):
    if n<=1:
        return n

    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

        return dp[n]

n=int(input("entern:"))
print(f"fibonacci((n))={fibonacci_tab(n)}")

