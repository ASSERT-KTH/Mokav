def func(*args):
	ret_values = []
	
	import sys
	string = args[0]
	cnt = v = 0
	s = ''
	if (len(string) == 1):
	    ret_values.append('0')
	elif (len(string) == 2):
	    if ('KV' in string):
	        ret_values.append('0')
	    else:
	        ret_values.append('1')
	else:
	    for i in range(0, (len(string) - 1)):
	        if (v == 1):
	            v = 0
	            continue
	        if ((string[i] == 'V') and (string[(i + 1)] == 'K')):
	            cnt += 1
	            v = 1
	            s += '0'
	        else:
	            s += string[i]
	            v = 0
	        if (i == (len(string) - 2)):
	            s += string[(len(string) - 1)]
	    if (('VV' in s) or ('KK' in s)):
	        cnt += 1
	    ret_values.append(cnt)

	return ret_values
