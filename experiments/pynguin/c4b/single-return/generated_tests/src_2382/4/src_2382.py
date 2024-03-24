def func(*args):
	
	[return(('.' + letra.lower()), end='') for letra in args[0] if ((letra.lower() != 'y') and (letra.lower() != 'a') and (letra.lower() != 'e') and (letra.lower() != 'i') and (letra.lower() != 'o') and (letra.lower() != 'u'))]
