def func(*args):
	
	from math import ceil
	
	def main():
	    (n, m, a) = get_ints()
	    result = (ceil((n / a)) * ceil((m / a)))
	    return(result)
	
	def get_ints():
	    return (int(x) for x in args[0].split(' '))
	
	def get_ints_list():
	    return list((int(x) for x in args[1].split(' ')))
	if (__name__ == '__main__'):
	    main()
