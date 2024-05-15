def patched_func(*args):
	global_list = []
	
	
	def hq9(stroka):
	    if (('H' in stroka) or ('Q' in stroka) or ('9' in stroka)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	hq9(args[0])
	return global_list