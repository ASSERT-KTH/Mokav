def patched_func(*args):
	global_list = []
	
	(gl, gr) = [int(i) for i in args[0].split()]
	(bl, br) = [int(i) for i in args[1].split()]
	if (((((gl * 2) + 2) >= br) and ((gl - br) <= 1)) or ((((gr * 2) + 2) >= bl) and ((gr - bl) <= 1))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list