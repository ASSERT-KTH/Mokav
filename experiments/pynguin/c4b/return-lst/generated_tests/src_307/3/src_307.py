def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    field = list()
	    field.append(list(map(str, args[0])))
	    field.append(list(map(str, args[1])))
	    field.append(list(map(str, args[2])))
	    field.append(list(map(str, args[3])))
	    book = ('#', '.')
	    flag = False
	    for i in range(3):
	        for j in range(3):
	            v = (((book.index(field[i][j]) + book.index(field[(i + 1)][j])) + book.index(field[i][(j + 1)])) + book.index(field[(i + 1)][(j + 1)]))
	            if (v != 2):
	                flag = True
	                break
	        if flag:
	            break
	    (ret_values.append('YES') if flag else ret_values.append('NO'))

	return ret_values
