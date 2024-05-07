def original_func(*args):
	global_list = []
	
	
	def palindrome(s):
	    x = 0
	    for i in range(int((len(s) / 2))):
	        if (s[i] != s[((len(s) - 1) - i)]):
	            if (x == 0):
	                x = 1
	            else:
	                x = 2
	                break
	    return x
	s = args[0]
	if ((palindrome(s) == 1) or (palindrome(s) == 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list