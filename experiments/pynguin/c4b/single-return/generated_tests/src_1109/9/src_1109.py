def func(*args):
	
	s = str(args[0])
	l = [s[0]]
	i = 1
	flag = True
	while (i < (len(s) - 2)):
	    if (s[i:(i + 3)] == 'dot'):
	        l.append('.')
	        i += 3
	    elif ((s[i:(i + 2)] == 'at') and flag):
	        l.append('@')
	        flag = False
	        i += 2
	    else:
	        l.append(s[i])
	        i += 1
	if (s[(- 3):] == 'dot'):
	    l = (l[:(- 1)] + ['d', 'o', 't'])
	elif (s[(- 4):(- 1)] == 'dot'):
	    l += [s[(- 1)]]
	elif ((s[(- 3):(- 1)] == 'at') and (s.count('at') == 1)):
	    l += [s[(- 1)]]
	elif (l[(- 1)] == '@'):
	    l += [s[(- 2)], s[(- 1)]]
	else:
	    l += [s[(- 2)], s[(- 1)]]
	return(''.join(l))
