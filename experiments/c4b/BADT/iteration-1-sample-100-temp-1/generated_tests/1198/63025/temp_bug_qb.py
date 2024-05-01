def original_func(*args):
	global_list = []
	
	
	def check_symbols(_str, _arr):
	    _res = False
	    for x in _str:
	        for y in _arr:
	            if (x == y):
	                _res = True
	    return _res
	_str = args[0]
	_arr = ['H', 'Q', '9', '+']
	if check_symbols(_str, _arr):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list