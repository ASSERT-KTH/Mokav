def func(*args):
	ret_values = []
	
	
	def solve(n, s):
	    st = set(s)
	    arr = [int(i) for i in st]
	    if (len(arr) > 2):
	        ret_values.append('NO')
	    elif ((len(arr) == 1) and (arr[0] != 4) and (arr[0] != 7)):
	        ret_values.append('NO')
	    elif ((len(arr) == 2) and ((arr[0] * arr[1]) != 28)):
	        ret_values.append('NO')
	    else:
	        x = sum([int(s[i]) for i in range((n // 2))])
	        y = sum([int(s[i]) for i in range((n // 2), n)])
	        if (x == y):
	            ret_values.append('YES')
	        else:
	            ret_values.append('NO')
	n = int(args[0])
	num = args[1]
	solve(n, num)

	return ret_values
