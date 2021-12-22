import sys
read= sys.stdin.readline

def sol(N,M,nums):
    nums= sorted(nums)
    def recurse(arr,n,N,M,remain):
        if n == M:
            for num in arr:
                print(num, end=' ')
            print()
            return
        else:
            for i in range(len(remain)):
                arr[n] = remain[i]
                recurse(arr,n+1,N,M,remain[:i]+remain[i+1:])
    return recurse([None]*M,0,N,M,nums)

N, M = map(int,read().split())
nums = map(int,read().split())

sol(N,M,nums)

