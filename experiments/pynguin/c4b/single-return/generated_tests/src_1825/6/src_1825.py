def func(*args):
	
	matrix = [[int(x) for x in args[0].split()] for i in range(5)]
	moves = 0
	for i in range(5):
	    for n in range(5):
	        if (matrix[i][n] == 1):
	            if (i != n):
	                moves = (abs((i - 2)) + abs((n - 2)))
	            elif (i == n):
	                if (n == 2):
	                    moves = 0
	                elif (i == n):
	                    moves = (abs((i - 2)) + abs((n - 2)))
	return(moves)
