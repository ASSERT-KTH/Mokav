def patched_func(*args):
	global_list = []
	
	
	def suerte(n):
	    n = str(n)
	    L = [0, 1, 2, 3, 5, 6, 8, 9]
	    for k in L:
	        if (str(k) in n):
	            return False
	    return True
	n = args[0]
	cont = 0
	for k in n:
	    if ((k == '4') or (k == '7')):
	        cont += 1
	if (suerte(cont) and (cont != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list