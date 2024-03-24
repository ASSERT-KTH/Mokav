def func(*args):
	ret_values = []
	
	import re
	m = re.match('^\\w{1,16}@(?P<hostname>\\w{1,16}(?:\\.\\w{1,16})*)(?:\\/\\w{1,16})?$', args[0])
	ret_values.append(('NO' if ((m == None) or (len(m.group('hostname')) > 32)) else 'YES'))

	return ret_values
