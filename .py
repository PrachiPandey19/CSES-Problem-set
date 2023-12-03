n=int(input())
mod=10**9+7 

dp=[0]*(n+1)
dp[0]=dp[1]=1
for i in range(2,n+1):
    if i<=6:dp[i]=2*dp[i-1]  
    else:dp[i]=(2*dp[i-1]-dp[i-7])%mod
print(dp[n]%mod)
