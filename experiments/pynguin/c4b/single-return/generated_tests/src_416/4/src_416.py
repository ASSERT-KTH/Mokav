def func(*args):
	
	rows = [list(map(int, args[0].split())) for x in range(4)]
	turns = [[0, 1, 2], [0], [1], [2]]
	results = 'NO'
	for x in range(4):
	    if rows[x][3]:
	        for y in range(4):
	            for z in turns[y]:
	                if rows[y][z]:
	                    results = 'YES'
	                    break
	    if (results == 'YES'):
	        break
	    turns.insert(0, turns[(- 1)])
	    del turns[(- 1)]
	return(results)
