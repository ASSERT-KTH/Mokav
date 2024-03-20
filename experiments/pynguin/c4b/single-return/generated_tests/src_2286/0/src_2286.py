def func(*args):
	
	import re
	return(('YES' if re.match('.*h.*e.*l.*l.*o.*', str(args[0])) else 'NO'))
