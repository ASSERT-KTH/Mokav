def func(*args):
	ret_values = []
	
	(x, y) = [int(x) for x in args[0].split()]
	
	def even_move(x, y):
	    if ((x >= 2) and (y >= 2)):
	        return [True, (x - 2), (y - 2)]
	    if ((x >= 1) and (y >= 12)):
	        return [True, (x - 1), (y - 12)]
	    if (y >= 22):
	        return [True, x, (y - 22)]
	    return [False, x, y]
	
	def odd_move(x, y):
	    if (y >= 22):
	        return [True, x, (y - 22)]
	    if ((x >= 1) and (y >= 12)):
	        return [True, (x - 1), (y - 12)]
	    if ((x >= 2) and (y >= 2)):
	        return [True, (x - 2), (y - 2)]
	    return [False, x, y]
	
	def game(x, y):
	    even = 'Ciel'
	    odd = 'Hanako'
	    i = 0
	    while True:
	        if ((i % 2) == 0):
	            move = even_move(x, y)
	            if move[0]:
	                x = move[1]
	                y = move[2]
	            else:
	                return odd
	        else:
	            move = odd_move(x, y)
	            if move[0]:
	                x = move[1]
	                y = move[2]
	            else:
	                return even
	        i += 1
	ret_values.append(game(x, y))

	return ret_values
