def sol():
    N = int (input())
    nums = list(map(int,input().split()))
    MAX_NUM = 1000000
    
    def prime_list(n): #참고 https://velog.io/@joygoround/test-unsolved-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
        sieve = [True] * n
        m = int(n**0.5)
        for i in range(2,m+1):
            if sieve[i] == True:
                for j in range(i+i, n, i):
                    sieve[j] = False
        return sieve

    isPrime = prime_list(MAX_NUM)
    value =1
    for num in nums:
        if isPrime[num]:
            isPrime[num] = False
            value *= num

    return value if value != 1 else -1

print(sol())
