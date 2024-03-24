def func(*args):
	
	i = args[0].split(' ')
	i = [int(a) for a in i]
	
	def gcd(a, b):
	    return (a if (b == 0) else gcd(b, (a % b)))
	return(((((i[0] // i[1]) * i[3]) + ((i[0] // i[2]) * i[4])) - ((i[0] // ((i[1] * i[2]) // gcd(i[1], i[2]))) * min(i[3], i[4]))))
