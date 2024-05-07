def patched_func(*args):
	global_list = []
	
	
	def larger(a, b):
	    if (a > b):
	        return a
	    else:
	        return b
	lisa = args[0]
	index = ([0] * len(lisa))
	if ('h' in lisa):
	    lisa = lisa[lisa.index('h'):]
	jin = ''
	for i in range(len(lisa)):
	    if ((lisa[i] == 'h') or (lisa[i] == 'e') or (lisa[i] == 'l') or (lisa[i] == 'o')):
	        jin += lisa[i]
	kate = ''
	count = 0
	for i in range(len(jin)):
	    if (jin[i] == 'h'):
	        count = i
	        kate += 'h'
	        break
	count2 = 0
	for i in range(count, len(jin)):
	    if (jin[i] == 'e'):
	        count2 = i
	        kate += 'e'
	        break
	count3 = 0
	for i in range(count2, len(jin)):
	    if (count3 > 0):
	        break
	    for j in range(count2, len(jin)):
	        if (((jin[i] + jin[j]) == 'll') and (i != j)):
	            count3 = larger(i, j)
	            kate += 'll'
	            break
	for i in range(count3, len(jin)):
	    if (jin[i] == 'o'):
	        kate += 'o'
	        break
	if (kate == 'hello'):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list