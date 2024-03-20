def func(*args):
	
	cad = args[0].lower()
	v = ['a', 'o', 'y', 'e', 'u', 'i']
	result = ''
	for i in cad:
	    if (i in v):
	        continue
	    else:
	        result = ((result + '.') + i)
	return(result)
