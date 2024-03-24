def func(*args):
	ret_values = []
	
	
	def palindrome(s):
	    x = 0
	    if (len(s) % 2):
	        for i in range(int((len(s) / 2))):
	            if (s[i] != s[((len(s) - 1) - i)]):
	                if (x == 0):
	                    x = 1
	                else:
	                    x = 2
	                    break
	        if (x == 0):
	            x = 1
	    else:
	        for i in range(int((len(s) / 2))):
	            if (s[i] != s[((len(s) - 1) - i)]):
	                if (x == 0):
	                    x = 1
	                else:
	                    x = 2
	                    break
	    return x
	s = args[0]
	if (palindrome(s) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
