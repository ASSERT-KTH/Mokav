def original_func(*args):
	global_list = []
	
	from sys import exit
	s = args[0]
	i = int(s)
	n = 0
	k = i
	while (k > 0):
	    n += 1
	    k //= 10
	if (n == 1):
	    global_list.append(s)
	    exit()
	k = 1
	l = (int(s[0]) * (10 ** (n - 1)))
	while (s[k] == '9'):
	    k += 1
	    l += (9 * (10 ** (n - k)))
	    if (k == (n - 1)):
	        global_list.append(s)
	        exit()
	l -= 1
	if (('0' in s[k:]) or ('1' in s[k:]) or ('2' in s[k:]) or ('3' in s[k:]) or ('4' in s[k:]) or ('5' in s[k:]) or ('6' in s[k:]) or ('7' in s[k:])):
	    global_list.append(l)
	elif ('8' in s[1:]):
	    p = s.find('8', 1)
	    if ('8' in s[(p + 1):]):
	        global_list.append(l)
	    else:
	        global_list.append(s)
	return global_list