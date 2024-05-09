def patched_func(*args):
	global_list = []
	
	In = args[0].split(' ')
	yw = max(int(In[0]), int(In[1]))
	num = len(range(yw, 7))
	den = 6
	
	def factor():
	    return [fac for fac in range(1, 7) if (((num % fac) == 0) and ((den % fac) == 0))]
	n = int((num / max(factor())))
	d = int((den / max(factor())))
	global_list.append('{}/{}'.format(n, d))
	return global_list