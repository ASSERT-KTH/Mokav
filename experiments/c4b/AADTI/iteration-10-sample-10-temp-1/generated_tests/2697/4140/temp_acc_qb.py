def patched_func(*args):
	global_list = []
	
	
	def mp():
	    return map(int, args[0].split())
	
	def lt():
	    return list(map(int, args[1].split()))
	
	def pt(x):
	    global_list.append(x)
	
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
	    global_list.append(' '.join([str(x) for x in l]))
	(a, b) = mp()
	(c, d) = mp()
	
	def pgcd(x, y):
	    if (x > y):
	        return pgcd(y, x)
	    if ((y % x) == 0):
	        return x
	    else:
	        return pgcd((y % x), x)
	if ((abs((b - d)) % pgcd(a, c)) != 0):
	    pt((- 1))
	else:
	    k = b
	    s = d
	    while (k != s):
	        if (k > s):
	            s += c
	        else:
	            k += a
	    pt(k)
	return global_list