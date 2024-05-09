def original_func(*args):
	global_list = []
	
	
	def longest(s):
	    n = len(s)
	    result = ''
	    i = 0
	    while (i < n):
	        a = i
	        b = (i + 1)
	        while ((a > (- 1)) and (b < n)):
	            if (s[a] == s[b]):
	                a = (a - 1)
	                b = (b + 1)
	            else:
	                break
	        if ((a < i) and (b > (i + 1))):
	            if (len(s[(a + 1):b]) > len(result)):
	                result = s[(a + 1):b]
	        i = (i + 1)
	    i = 1
	    while (i < (n - 1)):
	        a = (i - 1)
	        b = (i + 1)
	        while ((a > (- 1)) and (b < n)):
	            if (s[a] == s[b]):
	                a = (a - 1)
	                b = (b + 1)
	            else:
	                break
	        if ((a < (i - 1)) and (b > (i + 1))):
	            if (len(s[(a + 1):b]) > len(result)):
	                result = s[(a + 1):b]
	        i = (i + 1)
	    return result
	global_list.append(longest(args[0]))
	return global_list