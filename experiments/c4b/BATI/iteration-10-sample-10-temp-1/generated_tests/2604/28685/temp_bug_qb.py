def original_func(*args):
	global_list = []
	
	
	def cut(s):
	    if (str(s) == '0'):
	        return s
	    for (i, item) in enumerate(str(s)):
	        if (item != '0'):
	            return s[i:]
	    return ''
	
	def g(sn):
	    n = int(sn)
	    edge = ((len(sn) - 1) * 9)
	    res = ([0] * len(sn))
	    if (n == 18):
	        return n
	    if (n < 10):
	        return n
	    if ((sn[0] == '1') and (sn[1] < '8')):
	        return ('9' * (len(sn) - 1))
	    if (sn[1] < '8'):
	        return (str((int(sn[0]) - 1)) + ('9' * (len(sn) - 1)))
	    is8 = (- 1)
	    for s in range((len(sn) - 1)):
	        if (sn[(s + 1)] != '9'):
	            if (is8 != (- 1)):
	                if (is8 == 0):
	                    if (sn[1] < '8'):
	                        return ('9' * (len(sn) - 1))
	                    else:
	                        return (''.join([(str((int(sn[0]) - 1)) if ((int(sn[0]) - 1) > 0) else '')]) + ('9' * (len(sn) - 1)))
	                else:
	                    return ((cut(sn[:is8]) + '8') + ('9' * ((len(sn) - is8) - 1)))
	            if (sn[(s + 1)] == '8'):
	                is8 = s
	                continue
	            if (sn[(s + 1)] < '8'):
	                return ((sn[:s] + '8') + ('9' * ((len(sn) - s) - 1)))
	global_list.append(g(args[0]))
	return global_list