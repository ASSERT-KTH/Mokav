def patched_func(*args):
	global_list = []
	
	import string
	
	def determinant(a11, a12, a21, a22):
	    return ((a11 * a22) - (a21 * a12))
	first = [int(coeff) for coeff in args[0].split()]
	second = [int(coeff) for coeff in args[1].split()]
	rang = 2
	if (determinant(first[0], first[1], second[0], second[1]) == 0):
	    rang = 1
	tilda_rang = 2
	if ((determinant(first[0], first[2], second[0], second[2]) == 0) and (determinant(first[1], first[2], second[1], second[2]) == 0) and (rang == 1)):
	    tilda_rang = 1
	if (rang == 1):
	    if ((first[0] == 0) and (first[1] == 0) and (second[0] == 0) and (second[1] == 0)):
	        rang = 0
	        if ((first[2] == 0) and (second[2] == 0)):
	            tilda_rang = 0
	        else:
	            tilda_rang = 1
	if (rang != tilda_rang):
	    global_list.append('0')
	elif (rang == 2):
	    global_list.append('1')
	else:
	    global_list.append('-1')
	return global_list