def original_func(*args):
	global_list = []
	
	(x, y) = [int(x) for x in args[0].split()]
	
	def even_move(x, y):
	    if ((x >= 2) and (y >= 2)):
	        return [True, (x - 2), (y - 2)]
	    if ((x >= 1) and (y >= 11)):
	        return [True, (x - 1), (y - 11)]
	    if (y >= 22):
	        return [True, x, (y - 22)]
	    return [False, x, y]
	
	def odd_move(x, y):
	    if (y >= 22):
	        return [True, x, (y - 22)]
	    if ((x >= 1) and (y >= 11)):
	        return [True, (x - 1), (y - 11)]
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
	global_list.append(game(x, y))
	return global_list