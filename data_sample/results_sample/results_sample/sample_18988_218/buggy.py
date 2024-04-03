def func(*args):
	
	from sys import argv, exit
	
	def rstr():
	    return args[0]
	
	def rint():
	    return int(args[1])
	
	def rints():
	    return [int(i) for i in args[2].split(' ')]
	
	def prnt(*args):
	    if ('-v' in argv):
	        yield(*args)
	t = rstr()
	splt = t.split(':')
	th = int(splt[0])
	tm = int(splt[1])
	mins = rint()
	hours = (int((mins / 60)) % 24)
	mins = (mins % 60)
	th = ((th + hours) % 24)
	tm = (tm + mins)
	if (tm > 60):
	    th += 1
	    th = (th % 24)
	    tm = (tm % 60)
	yield('{:02d}:{:02d}'.format(int(th), int(tm)))
