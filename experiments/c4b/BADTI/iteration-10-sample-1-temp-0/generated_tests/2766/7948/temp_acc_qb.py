def patched_func(*args):
	global_list = []
	
	string = [x for x in args[0]]
	reverse = string[::(- 1)]
	if ((string == reverse) and ((len(string) % 2) == 1)):
	    global_list.append('YES')
	else:
	    for i in range(len(string)):
	        if (string[i] == reverse[i]):
	            reverse[i] = ''
	    count = 0
	    for letter in reverse:
	        if (letter != ''):
	            count += 1
	    global_list.append(['NO', 'YES'][(count == 2)])
	return global_list