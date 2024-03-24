def func(*args):
	
	x = int(args[0])
	k = 0
	suma = 0
	casa = 1234567
	carro = 123456
	computadora = 1234
	mensaje = 'NO'
	while (x >= computadora):
	    a = x
	    b = x
	    c = x
	    d = x
	    e = x
	    f = x
	    if (x >= casa):
	        if (((x % casa) == 0) or ((x % computadora) == 0) or ((x % carro) == 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	        if ((x % casa) == 0):
	            mensaje = 'YES'
	            x = (computadora - 1)
	        if (((x % computadora) == 0) or ((x % carro) == 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	        x = (x - casa)
	    if ((x >= carro) and (x < casa)):
	        if ((x % carro) == 0):
	            mensaje = 'YES'
	            x = (computadora - 1)
	        if ((x % computadora) == 0):
	            mensaje = 'YES'
	            x = (computadora - 1)
	        x = (x - carro)
	    if ((x >= computadora) and (x < carro)):
	        x = (x - computadora)
	        if ((x % computadora) == 0):
	            mensaje = 'YES'
	            x = (computadora - 1)
	    while ((a and b) >= computadora):
	        a = (a - computadora)
	        b = (b - carro)
	        if ((((a % casa) == 0) or ((b % casa) == 0)) and ((a and b) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            a = (computadora - 1)
	        if (((((a - carro) % casa) == 0) or (((b - computadora) % casa) == 0)) and (((a - carro) and (b - computadora)) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            a = (computadora - 1)
	    while ((c and d) >= computadora):
	        c = (c - computadora)
	        d = (d - casa)
	        if ((((c % carro) == 0) or ((d % carro) == 0)) and ((c and d) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            c = (computadora - 1)
	        if (((((c - casa) % carro) == 0) or (((d - computadora) % carro) == 0)) and (((c - casa) and (d - computadora)) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            c = (computadora - 1)
	    while ((e and f) >= computadora):
	        e = (e - casa)
	        f = (f - carro)
	        if ((((e % computadora) == 0) or ((f % computadora) == 0)) and ((e and f) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            e = (computadora - 1)
	        if (((((e - carro) % computadora) == 0) or (((f - casa) % computadora) == 0)) and (((e - carro) and (f - casa)) > 0)):
	            mensaje = 'YES'
	            x = (computadora - 1)
	            e = (computadora - 1)
	return(mensaje)
