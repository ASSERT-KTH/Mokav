def func(*args):
	ret_values = []
	
	[ret_values.append(('.' + letra.lower()), end='') for letra in args[0] if ((letra.lower() != 'y') and (letra.lower() != 'a') and (letra.lower() != 'e') and (letra.lower() != 'i') and (letra.lower() != 'o') and (letra.lower() != 'u'))]

	return ret_values
