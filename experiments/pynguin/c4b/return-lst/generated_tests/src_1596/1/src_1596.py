def func(*args):
	ret_values = []
	
	(hobbits_nr, pillows_nr, frodos_place) = (int(x) for x in args[0].split())
	pillows_nr = (pillows_nr - hobbits_nr)
	frodos_pillows = 1
	left = frodos_place
	right = (frodos_place + 1)
	while (pillows_nr >= (right - left)):
	    pillows_nr -= (right - left)
	    frodos_pillows += 1
	    right += 1
	    left += (- 1)
	    if (right > (hobbits_nr + 1)):
	        right = (hobbits_nr + 1)
	    if (left < 1):
	        left = 1
	    if ((left == 1) and (right == (hobbits_nr + 1))):
	        frodos_pillows += (pillows_nr // hobbits_nr)
	        pillows_nr = (pillows_nr % hobbits_nr)
	ret_values.append(frodos_pillows)

	return ret_values
