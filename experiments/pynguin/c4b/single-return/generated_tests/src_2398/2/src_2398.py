def func(*args):
	
	a = args[0]
	a = a.lower()
	x = ''
	for i in range(len(a)):
	    if ((a[i] == 'a') or (a[i] == 'e') or (a[i] == 'i') or (a[i] == 'o') or (a[i] == 'u') or (a[i] == 'y')):
	        x += ''
	    else:
	        x += ('.' + a[i])
	return(x)
