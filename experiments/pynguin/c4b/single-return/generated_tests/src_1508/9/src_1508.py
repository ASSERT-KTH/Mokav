def func(*args):
	
	m = [[int(j) for j in args[0].split()] for i in range(5)]
	movs = 0
	while (m[2][2] != 1):
	    for i in range(5):
	        for j in range(5):
	            if ((m[i][j] == 1) and (i != 2)):
	                if (i > 2):
	                    m[i][j] = 0
	                    m[(i - 1)][j] = 1
	                    movs += 1
	                elif (i < 2):
	                    m[i][j] = 0
	                    m[(i + 1)][j] = 1
	                    movs += 1
	            if ((m[i][j] == 1) and (j != 2)):
	                if (j > 2):
	                    m[i][j] = 0
	                    m[i][(j - 1)] = 1
	                    movs += 1
	                elif (j < 2):
	                    m[i][j] = 0
	                    m[i][(j + 1)] = 1
	                    movs += 1
	return(movs)
