def func(*args):
	ret_values = []
	
	
	def solution():
	    string = args[0]
	    res = 0
	    for i in range(len(string)):
	        for j in range((i + 1), (len(string) + 1)):
	            tmp = 0
	            buf = string[i:j]
	            for k in range(((len(string) - len(buf)) + 1)):
	                if (buf == string[k:(k + len(buf))]):
	                    tmp += 1
	            if (tmp > 1):
	                res = max(res, len(buf))
	    return res
	ret_values.append(solution(), end='')

	return ret_values
