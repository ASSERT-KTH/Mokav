def original_func(*args):
	global_list = []
	
	string = args[0]
	l = 0
	for i in string:
	    if i.isupper():
	        l += 1
	result = string
	if ((l == len(string)) or (l == (len(string) - 1))):
	    result = ''
	    for i in string:
	        if i.islower():
	            result += i.upper()
	        else:
	            result += i.lower()
	global_list.append(result)
	return global_list