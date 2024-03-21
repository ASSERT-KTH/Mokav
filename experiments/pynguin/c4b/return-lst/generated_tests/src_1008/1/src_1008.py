def func(*args):
	ret_values = []
	
	string = [x for x in args[0]]
	reverse = string[::(- 1)]
	if ((string == reverse) and ((len(string) % 2) == 1)):
	    ret_values.append('YES')
	else:
	    for i in range(len(string)):
	        if (string[i] == reverse[i]):
	            reverse[i] = ''
	    count = 0
	    for letter in reverse:
	        if (letter != ''):
	            count += 1
	    ret_values.append(['NO', 'YES'][(count == 2)])

	return ret_values
