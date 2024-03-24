def func(*args):
	
	a = int(args[0])
	x = ''
	while a:
	    if (a % 2):
	        x = ('that I hate ' + x)
	    else:
	        x = ('that I love ' + x)
	    a -= 1
	return((x[5:] + 'it'))
