class Solution:
    #sieve of erasthosthenes
    def countPrimes(self, n: int) -> int:
        prime = [0]*n
        for i in range(4,n,2):
            prime[i] = 1
        for i in range(3,int(n**.5)+1,2):
            if prime[i] == 0:
                for j in range(i*i,n,i):
                    prime[j] = 1
        prime_count = 0
        for i in range(2,n):
            if prime[i] == 0:
                prime_count += 1
        if n==0 or n==1:
            return 0
        return prime_count
        