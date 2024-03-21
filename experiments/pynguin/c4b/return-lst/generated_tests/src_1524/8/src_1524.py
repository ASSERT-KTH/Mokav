def func(*args):
	ret_values = []
	
	s = str(args[0])
	p = ['h', 'e', 'l', 'l', 'o']
	
	def compare(inputArray, compareArray):
	    temp = 0
	    n = len(inputArray)
	    for item in compareArray:
	        while (temp <= n):
	            if (s[temp] == item):
	                if (item == p[(len(p) - 1)]):
	                    return ret_values.append('YES')
	                elif ((item != p[(len(p) - 1)]) and (temp == (n - 1))):
	                    return ret_values.append('NO')
	                temp += 1
	                break
	            elif (temp == (n - 1)):
	                return ret_values.append('NO')
	            temp += 1
	compare(s, p)

	return ret_values
