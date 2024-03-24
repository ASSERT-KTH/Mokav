def func(*args):
	ret_values = []
	
	s = args[0]
	n = len(s)
	cnt = 0
	flag = 1
	light = [1 for j in range(n)]
	i = 0
	while (i < n):
	    if ((i < (n - 1)) and (s[i] == 'V') and (s[(i + 1)] == 'K')):
	        cnt += 1
	        light[i] = light[(i + 1)] = 0
	        i += 2
	    else:
	        i += 1
	i = 0
	while ((i < n) and flag):
	    if ((i < (n - 1)) and (s[i] == 'V') and (s[(i + 1)] == 'V') and light[i] and light[(i + 1)]):
	        cnt += 1
	        flag = 0
	    elif ((i < (n - 1)) and (s[i] == 'K') and (s[(i + 1)] == 'K') and light[i] and light[(i + 1)]):
	        cnt += 1
	        flag = 0
	    else:
	        i += 1
	ret_values.append(cnt)

	return ret_values
