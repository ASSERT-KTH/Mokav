def func(*args):
	ret_values = []
	
	(gl, gr) = [int(i) for i in args[0].split()]
	(bl, br) = [int(i) for i in args[1].split()]
	if (((((gl * 2) + 2) >= br) and ((gl - br) <= 1)) or ((((gr * 2) + 2) >= bl) and ((gr - bl) <= 1))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
