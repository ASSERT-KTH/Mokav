def func(*args):
	ret_values = []
	
	import re
	import inspect
	from sys import argv, exit
	
	def rstr():
	    return args[0]
	
	def rint():
	    return int(args[1])
	
	def rints(splitchar=' '):
	    return [int(i) for i in args[2].split(splitchar)]
	
	def varnames(obj, namespace=globals()):
	    return [name for name in namespace if (namespace[name] is obj)]
	
	def pvar(var, override=False):
	    prnt(varnames(var), var)
	
	def prnt(*args, override=False):
	    if (('-v' in argv) or override):
	        ret_values.append(*args)
	if (__name__ == '__main__'):
	    n = rint()
	    k = 2
	    if (n >= 13):
	        n -= 13
	        ret_values.append((8092 * (k ** n)))
	        exit(0)
	    ret_values.append((k ** n))

	return ret_values
