def func(*args):
	ret_values = []
	
	
	def hq9(stroka):
	    if (('H' in stroka) or ('Q' in stroka) or ('9' in stroka)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	hq9(args[0])

	return ret_values
