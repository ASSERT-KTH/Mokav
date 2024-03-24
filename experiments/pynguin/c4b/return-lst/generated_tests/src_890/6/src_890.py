def func(*args):
	ret_values = []
	
	'x=int(input())\n\ni=1\n\nwhile 1:\n\n    y=x\n\n    y=(y-(2*i))/2\n\n    if y<=i:\n\n        break\n\n    i+=1\n\ni-=1\n\nret_values.append(i)\n\n'
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append(0)
	else:
	    m = (n // 2)
	    if ((m % 2) == 0):
	        m -= 1
	    ret_values.append((m // 2))

	return ret_values
