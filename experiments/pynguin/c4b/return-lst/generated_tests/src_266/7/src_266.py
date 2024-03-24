def func(*args):
	ret_values = []
	
	
	def is_subseq(a, b):
	    it = iter(b)
	    return all(((c in it) for c in a))
	if is_subseq('hello', args[0]):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
