def patched_func(*args):
	global_list = []
	
	import re
	m = re.match('^\\w{1,16}@(?P<hostname>\\w{1,16}(?:\\.\\w{1,16})*)(?:\\/\\w{1,16})?$', args[0])
	global_list.append(('NO' if ((m == None) or (len(m.group('hostname')) > 32)) else 'YES'))
	return global_list