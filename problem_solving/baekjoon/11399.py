# 백준 11399

n = int(input())
p = list(map(int, input().split()))

# if 배열 == [3, 2, 1, 3] then,
# 최솟값 == 3*4 + 2*3 + 1*2 + 3*1
p.sort()
ans = 0
for i in range(n):
    ans += (i+1) * p[-(i+1)]
    
print(ans)