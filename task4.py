n, m = map(int, input().split())
 
lab = []
for i in range(n):
    vr_ls = [int(s) for s in input().split()]
    lab.append(vr_ls)
 
a, b = map(int, input().split())
 
 
 
for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 0:
            lab[i][j] = -1
        elif lab[i][j] == 1:
            lab[i][j] = -2
 
 
lab[0][0] = 0
 
t = t_vr = [(0, 0)]
 
while len(t) != 0 and (a, b) not in t:
    koo = t[len(t) - 1]
    i, j = koo[0], koo[1]
    count = lab[i][j] + 1

	if i > 0 and lab[i-1][j] == -1:
	    lab[i-1][j] = count
	    t_vr.append((i-1, j))
	elif i < n - 1 and lab[i+1][j] == -1:
	    lab[i+1][j] = count
	    t_vr.append((i+1, j))
	elif j > 0 and lab[i][j-1] == -1:
	    lab[i][j-1] = count
	    t_vr.append((i, j-1))
	elif j < m - 1 and lab[i][j+1] == -1:
	    lab[i][j+1] = count
	    t_vr.append((i, j+1))
    else: # откат к предыдущей точке
    	t_vr.pop(len(t_vr) - 1)
    	count -= 1
 
    t = t_vr
 
# print(lab[a][b]) верно, но можно учесть случай, если в качестве (a, b) подали стенку
if lab[a][b] == -2:
	print(-1)
else:
	print(lab[a][b])
