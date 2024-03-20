def func(*args):
	
	
	def gcd(a, b):
	    if (a == 0):
	        return b
	    return gcd((b % a), a)
	l = list(map(int, args[0].split()))
	t = l[0]
	w = l[1]
	b = l[2]
	ans = 0
	lcm = ((w * b) // gcd(w, b))
	mul = (t // lcm)
	if (w > b):
	    temp = w
	    w = b
	    b = temp
	if (t < (((lcm * mul) + w) - 1)):
	    ans = ((t - (lcm * mul)) + 1)
	else:
	    ans = w
	ans += ((mul * w) - 1)
	g2 = gcd(ans, t)
	return((ans // g2), '/', (t // g2), sep='')
