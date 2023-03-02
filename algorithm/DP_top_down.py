# Memoization할 리스트 선언
memo = []

def fib(n):
    # fib(2), fib(1) 호출 시 정수(1) return
    if n <= 2:
        return 1
    
    else:
        # 재귀를통해 fib(5), fib(4), …  (큰 문제 -> 작은 문제) 순으로 호출 후,
        # 작은 문제들의 값을 return 받아 큰 문제에 활용
        memo.append(fib(n-1) + fib(n-2))
        # 직전에 계산한 값을 return
        return memo[-1]
        
# 입력 및 출력
print(fib(int(input())))