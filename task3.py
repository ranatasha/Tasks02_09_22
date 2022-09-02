n, m, a = list(map(int, input().split()))
my_list = []
sm = 0
x = 0
y = 0
b = 1
c = 1
d = 1
e = 1
for g in range(n):
    my_list.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if my_list[i][j] == a:
            x = i
            y = j
            break
if y == 0:
    if x == 0:
        b = my_list[x + 1][y + 1]
    elif x == n - 1:
        b = my_list[x - 1][y + 1]
    else:
        b = my_list[x + 1][y + 1]
        c = my_list[x - 1][y + 1]
elif y == m - 1:
    if x == 0:
        b = my_list[x + 1][y - 1]
    elif x == n - 1:
        b = my_list[x - 1][y - 1]
    else:
        b = my_list[x + 1][y - 1]
        c = my_list[x - 1][y - 1]
else:
    if x != 0 and x != m - 1:
        b = my_list[x + 1][y + 1]
        c = my_list[x - 1][y + 1]
        d = my_list[x + 1][y - 1]
        e = my_list[x - 1][y - 1]
    elif x == 0:
    	b = my_list[x + 1][y - 1] 
        c = my_list[x + 1][y + 1] 
    else: 
        b = my_list[x - 1][y - 1] # сверху слева
        c = my_list[x - 1][y + 1] # сверху справа
print(b * c * d * e)
