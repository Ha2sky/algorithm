def fib(n):
    # Memoization할 리스트 선언 및 fib(0), fib(1) 값 설정
    memo = []
    memo.append(0)
    memo.append(1)
    
    # 반복문을 통해 fib(2), fib(3), … 작은 문제부터 해결
    for i in range(2, n+1):
	    # 구한 값을 memo 리스트에 Memoization
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]

# 입력 및 출력
print(fib(int(input())))