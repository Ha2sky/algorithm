import sys
sys.stdin = open(r"C:\Users\qkrwh\Documents\Python Scripts\test\input.txt", "r")
arr = [list(map(int, sys.stdin.readline().split())) for i in range(9)]

# 비어있는 좌표를 기록
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))

# arr[x][y]에 num이 가능한지 확인
def chk(x, y, num):
    subX = x // 3 * 3
    subY = y // 3 * 3
    for q in range(3):
        for w in range(3):
            if arr[subX + q][subY + w] == num or arr[x][q*3+w] == num or arr[q*3+w][y] == num:
                return False
    return True

def dfs(s):
    if s == len(blank):
        for q in range(9):
            print(*arr[q])
        sys.exit()
    
    for num in range(1, 10):
        x, y = blank[s][0], blank[s][1]
        if chk(x, y, num):
            arr[x][y] = num
            dfs(s+1)
            arr[x][y] = 0
            
dfs(0)