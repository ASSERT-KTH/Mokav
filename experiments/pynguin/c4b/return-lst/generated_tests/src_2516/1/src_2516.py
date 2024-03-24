def func(*args):
	ret_values = []
	
	from math import ceil
	from decimal import Decimal
	(n, m) = map(int, args[0].split())
	barn = n
	if (n <= m):
	    ret_values.append(n)
	else:
	    days = ceil((((- 1) + (Decimal((1 + (8 * (n - m)))) ** Decimal(0.5))) / 2))
	    ret_values.append((days + m))

	return ret_values
