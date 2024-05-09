def original_func(*args):
	global_list = []
	
	
	def main():
	    s = args[0]
	    flag = 'hello'
	    id = 0
	    for i in flag:
	        a = s.find(i, id, (len(s) - id))
	        if (a == (- 1)):
	            return False
	        id = a
	    return True
	ans = main()
	if ans:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list