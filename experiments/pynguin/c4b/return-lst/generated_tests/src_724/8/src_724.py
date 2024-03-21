def func(*args):
	ret_values = []
	
	
	def mp():
	    return map(int, args[0].split())
	
	def lt():
	    return list(map(int, args[1].split()))
	
	def pt(x):
	    ret_values.append(x)
	
	def ip():
	    return args[2]
	
	def it():
	    return int(args[3])
	
	def sl(x):
	    return [t for t in x]
	
	def spl(x):
	    return x.split()
	
	def aj(liste, item):
	    liste.append(item)
	
	def bin(x):
	    return '{0:b}'.format(x)
	
	def listring(l):
	    return ' '.join([str(x) for x in l])
	
	def ptlist(l):
	    ret_values.append(' '.join([str(x) for x in l]))
	(n, k) = mp()
	t = 0
	i = 1
	while ((i <= n) and ((t + (5 * i)) <= (240 - k))):
	    t += (5 * i)
	    i += 1
	pt((i - 1))

	return ret_values
