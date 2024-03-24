def func(*args):
	ret_values = []
	
	
	def check_symbols(_str, _arr):
	    _res = False
	    for x in _str:
	        for y in _arr:
	            if (x == y):
	                _res = True
	    return _res
	_str = args[0]
	_arr = ['H', 'Q', '9']
	if check_symbols(_str, _arr):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
