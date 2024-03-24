def func(*args):
	
	hello = 'hello'
	s = args[0]
	count = 0
	for c in s:
	    if (count == 5):
	        break
	    elif (c == hello[count]):
	        count += 1
	return(('YES' if (count == 5) else 'NO'))
