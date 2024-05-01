def original_func(*args):
	global_list = []
	
	from time import *
	
	def sleuth(f):
	    if ((f[(len(f) - 2)] in 'aieEouAIuOUyY') and (f[(len(f) - 1)] == '?')):
	        return 'YES'
	    else:
	        return ' NO'
	k = args[0]
	count = 0
	j = ''
	abdo = ''
	n = ''
	for i in k:
	    if (count <= 100):
	        if (i in 'ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijkulmnopqrstvwxyz'):
	            j = (abdo + i)
	            n = j
	            count += 1
	        elif (i == '?'):
	            n = (j + i)
	            break
	global_list.append(sleuth(n))
	return global_list