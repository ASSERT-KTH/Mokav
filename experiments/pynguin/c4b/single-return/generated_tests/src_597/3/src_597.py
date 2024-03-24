def func(*args):
	
	MOD = ((10 ** 9) + 7)
	mat = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
	matt = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	matb = ([mat] + [[([0] * 4) for _ in range(4)] for _ in range(30)])
	for x in range(1, 30):
	    for i in range(4):
	        for j in range(4):
	            for k in range(4):
	                matb[x][i][j] = ((matb[x][i][j] + (matb[(x - 1)][i][k] * matb[(x - 1)][k][j])) % MOD)
	n = int(args[0])
	t = 0
	while n:
	    matm = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	    if (n % 2):
	        for i in range(4):
	            for j in range(4):
	                for k in range(4):
	                    matm[i][j] = ((matm[i][j] + (matt[i][k] * matb[t][k][j])) % MOD)
	        matt = matm
	    n //= 2
	    t += 1
	return(matt[0][0])
