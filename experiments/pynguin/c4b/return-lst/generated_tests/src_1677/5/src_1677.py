def func(*args):
	ret_values = []
	
	import sys
	
	def add_zeros(maxs, mins):
	    diff = (len(maxs) - len(mins))
	    s0 = (diff * '0')
	    return (s0 + mins)
	
	def result(_xor, _sum, flag):
	    if ((len(_xor) + len(_sum)) == 0):
	        return (0 if flag else 1)
	    s = (_xor[(- 1)] + _sum[(- 1)])
	    newxor = _xor[:(- 1)]
	    newsum = _sum[:(- 1)]
	    if (s == '00'):
	        return (0 if flag else (result(newxor, newsum, True) + result(newxor, newsum, False)))
	    if (s == '11'):
	        return (0 if flag else (2 * result(newxor, newsum, False)))
	    if (s == '10'):
	        return ((2 * result(newxor, newsum, True)) if flag else 0)
	    if (s == '01'):
	        return ((result(newxor, newsum, True) + result(newxor, newsum, False)) if flag else 0)
	(ss, xr) = [int(x) for x in sys.stdin.readline().split()]
	_sum = bin(ss).split('b')[1]
	_xor = bin(xr).split('b')[1]
	if (len(_sum) > len(_xor)):
	    _xor = add_zeros(_sum, _xor)
	else:
	    _sum = add_zeros(_xor, _sum)
	res = result(_xor, _sum, False)
	ret_values.append(((res - 2) if (ss == xr) else res))

	return ret_values
