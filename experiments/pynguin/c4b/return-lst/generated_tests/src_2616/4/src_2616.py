def func(*args):
	ret_values = []
	
	string = args[0]
	ln = len(string)
	if (ln == 1):
	    ret_values.append(0)
	elif (ln == 2):
	    if (string != 'KV'):
	        ret_values.append(1)
	    else:
	        ret_values.append(0)
	else:
	    chang = ['VVV', 'KKK']
	    add = 0
	    for i in chang:
	        if string.count(i):
	            add = 1
	            break
	    if ((string[:3] == 'KKV') or (string[(- 3):] == 'KVV')):
	        add = 1
	    ret_values.append((string.count('VK') + add))

	return ret_values
