def func(*args):
	
	horseshoes_color = args[0].split()
	count = (len(horseshoes_color) - len(list(set(horseshoes_color))))
	return(count)
