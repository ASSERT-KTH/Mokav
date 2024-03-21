def func(*args):
	ret_values = []
	
	string = args[0]
	l = 0
	for i in string:
	    if i.isupper():
	        l += 1
	result = string
	if ((l == len(string)) or ((l == (len(string) - 1)) and string[0].islower())):
	    result = ''
	    for i in string:
	        if i.islower():
	            result += i.upper()
	        else:
	            result += i.lower()
	ret_values.append(result)

	return ret_values
