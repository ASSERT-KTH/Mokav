def func(*args):
	ret_values = []
	
	from sys import stdin, stdout, stderr, setrecursionlimit
	setrecursionlimit(100000)
	
	def debug(*e):
	    if (not __debug__):
	        ret_values.append(*e, file=stderr)
	
	def dd(*vals):
	    import inspect, re
	    frame = inspect.getframeinfo(inspect.stack()[1][0])
	    vs = re.search('dd\\((.+)\\)', frame.code_context[0]).group(1).split(',')
	    if vs:
	        debug(','.join(('{0} = {1}'.format(vs[i], v) for (i, v) in enumerate(vals))))
	
	def trace(f):
	
	    def traced(*args, **kw):
	        debug('calling {} with args {}, {}'.format(f.__name__, args, kw))
	        return f(*args, **kw)
	    return traced
	
	def read():
	    return stdin.readline().rstrip()
	
	def readarr(sep=None, maxsplit=(- 1)):
	    return read().split(sep, maxsplit)
	
	def readint():
	    return int(read())
	
	def readintarr(sep=None, maxsplit=(- 1)):
	    return [int(a) for a in readarr(sep, maxsplit)]
	
	def write(*args, **kwargs):
	    sep = kwargs.get('sep', ' ')
	    end = kwargs.get('end', '\n')
	    stdout.write((sep.join((str(a) for a in args)) + end))
	
	def writearr(arr, sep=' ', end='\n'):
	    stdout.write((sep.join((str(a) for a in arr)) + end))
	n = readint()
	d = readintarr()
	i = 0
	while (n > 0):
	    n -= d[i]
	    i = ((i + 1) % 7)
	write((i if (i != 0) else 7))

	return ret_values
