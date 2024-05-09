def original_func(*args):
	global_list = []
	
	
	def cnt(s, p):
	    ans = 0
	    if (p > s):
	        ans = 0
	    elif (len(p) == len(s)):
	        ans = (1 if (len(set(p.lstrip('0'))) <= 2) else 0)
	    elif (len(set(p.lstrip('0'))) > 2):
	        ans = 0
	    elif (s[:len(p)] > p):
	        if (len(set(p.lstrip('0'))) == 2):
	            ans = (2 ** (len(s) - len(p)))
	        elif (len(set(p.lstrip('0'))) == 1):
	            ans = (1 + (9 * ((2 ** (len(s) - len(p))) - 1)))
	        else:
	            ans = (10 + (45 * ((2 ** (len(s) - len(p))) - 2)))
	    else:
	        ans = sum((cnt(s, (p + c)) for c in '0123456789'))
	    return ans
	global_list.append((cnt(args[0].strip(), '') - 1))
	return global_list