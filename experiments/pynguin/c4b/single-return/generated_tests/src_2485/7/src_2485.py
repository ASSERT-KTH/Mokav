def func(*args):
	
	if (__name__ == '__main__'):
	    cyclicPathLength = int(args[0])
	    a = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
	    b = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	    while (cyclicPathLength != 0):
	        if (int((cyclicPathLength % 2)) == 1):
	            c = [([0] * 4) for i in range(4)]
	            for i in range(4):
	                for j in range(4):
	                    for k in range(4):
	                        c[i][j] += (a[i][k] * b[k][j])
	                    c[i][j] %= 1000000007
	            b = c
	        c = [([0] * 4) for i in range(4)]
	        for i in range(4):
	            for j in range(4):
	                for k in range(4):
	                    c[i][j] += (a[i][k] * a[k][j])
	                c[i][j] %= 1000000007
	        a = c
	        cyclicPathLength /= 2
	    return(b[0][0])
