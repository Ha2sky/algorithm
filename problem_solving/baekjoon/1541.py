# 백준 1541

# Ex) 30+30-50-40+40-30
arr = input().split('-')

var = []
# arr = ['30+30', '50', '40+30', '30']
for i in arr:
    temp = 0
    i = i.split('+')
    # i = ['30' ,'30'], ['50'], ['40', '40'], ['30']
    for j in i: 
        temp += int(j)
    # var = [60, 50, 80, 30]
    var.append(temp)
        
# print(60 - 150)
print(var[0] - sum(var[1:]))