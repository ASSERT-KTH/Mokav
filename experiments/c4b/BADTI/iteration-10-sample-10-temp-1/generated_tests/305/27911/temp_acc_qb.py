def patched_func(*args):
	global_list = []
	
	import io
	import sys
	import time
	import random
	(s, x) = list(map(int, args[0].split()))
	bitlen = s.bit_length()
	
	def bits_of(x, bitlen):
	    return [int((((1 << i) & x) != 0)) for i in range(bitlen)]
	sbits = bits_of(s, bitlen)
	xbits = bits_of(x, bitlen)
	overflows = bits_of((s ^ x), (bitlen + 1))
	count = 1
	if ((overflows[0] != 0) or (s < x)):
	    count = 0
	else:
	    zero_is_solution = True
	    for i in range(bitlen):
	        sumof_a_and_b = (((2 * overflows[(i + 1)]) + sbits[i]) - overflows[i])
	        if (((sumof_a_and_b == 0) and (xbits[i] == 1)) or ((sumof_a_and_b == 1) and (xbits[i] == 0)) or ((sumof_a_and_b == 2) and (xbits[i] == 1)) or (sumof_a_and_b > 2) or (sumof_a_and_b < 0)):
	            count = 0
	            break
	        if ((sumof_a_and_b == 1) and (xbits[i] == 1)):
	            count *= 2
	        if ((sumof_a_and_b == 2) and (xbits[i] == 0)):
	            zero_is_solution = False
	if ((count > 0) and zero_is_solution):
	    count -= 2
	global_list.append(count)
	return global_list