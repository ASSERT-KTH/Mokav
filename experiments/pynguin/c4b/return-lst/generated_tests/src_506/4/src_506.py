def func(*args):
	ret_values = []
	
	
	def main():
	    s = args[0]
	    flag = 'hello'
	    id = (- 1)
	    for i in flag:
	        a = s.find(i, (id + 1))
	        if (a == (- 1)):
	            return False
	        id = a
	    return True
	ans = main()
	if ans:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
