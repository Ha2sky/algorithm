# 백준 13305

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 반복문으로 도시(price)를 지나치며 최소 기름값 갱신(min)
min = price[0]
ans = 0
for i in range(n - 1):
    if min > price[i]:
        min = price[i]
    ans += min * distance[i]
    
print(ans)