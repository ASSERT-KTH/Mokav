def func(*args):
	ret_values = []
	
	
	def str_finder(s):
	    counter = counter_str(s)
	    for i in range(len(s)):
	        if (s[i] == 'V'):
	            new = ((s[:i] + 'K') + s[(i + 1):])
	        else:
	            new = ((s[:i] + 'V') + s[(i + 1):])
	        if (counter_str(new) > counter):
	            counter = counter_str(new)
	    return counter
	
	def counter_str(s):
	    count = 0
	    for i in range((len(s) - 1)):
	        if ((s[i] == 'V') and (s[(i + 1)] == 'K')):
	            count += 1
	    return count
	if (__name__ == '__main__'):
	    n = str(args[0])
	    ret_values.append(str_finder(n))

	return ret_values
