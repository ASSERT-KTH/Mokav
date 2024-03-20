def func(*args):
	
	a = args[0]
	c = int(args[1])
	o = (c // 60)
	p = (c % 60)
	kasra = int(a[3:])
	kasra += p
	if (kasra >= 60):
	    o += (kasra // 60)
	    kasra -= 60
	    if (kasra < 10):
	        kasra = ('0' + str(kasra))
	    else:
	        kasra = str(kasra)
	if (len(str(kasra)) == 1):
	    kasra = ('0' + str(kasra))
	else:
	    kasra = str(kasra)
	z = int(a[:2])
	z += o
	if (z >= 24):
	    z -= (24 * (z // 24))
	if (z < 10):
	    z = ('0' + str(z))
	z = str(z)
	g = ((z + ':') + kasra)
	return(g)
