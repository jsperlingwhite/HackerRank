# so i'm already pretty familiar with recursion, so i figured
# let's use dynamic programming instead.
# this solution is not at all more efficient than the recommended one.
# it just has hashtables and dynamic programming.

dp = {}
def factorial(n):
    if n==1:
        return 1
    if n-1 in dp:
        dp[n]=n*dp[n-1]
        return n*dp[n-1]
    else: #n-1 not in d
        x = factorial(n-1)
        dp[n-1]=x
        dp[n]=n*x
        return n*x

def main():
    n = int(raw_input())
    print factorial(n)

if __name__=="__main__":
    main()
