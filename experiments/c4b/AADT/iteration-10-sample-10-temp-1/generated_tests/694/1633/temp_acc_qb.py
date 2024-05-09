def patched_func(*args):
	global_list = []
	
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	string = args[0]
	column = (letters.index(string[0]) + 1)
	row = int(string[1])
	moves = 8
	condition1 = (column == row == 1)
	condition2 = (column == row == 8)
	condition3 = ((column == 1) and (row == 8))
	condition4 = ((column == 8) and (row == 1))
	if (condition1 or condition2 or condition3 or condition4):
	    moves -= 5
	elif ((column == 1) or (column == 8) or (row == 1) or (row == 8)):
	    moves -= 3
	global_list.append(moves)
	return global_list