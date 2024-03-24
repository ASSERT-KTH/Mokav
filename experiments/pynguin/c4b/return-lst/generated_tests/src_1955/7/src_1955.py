def func(*args):
	ret_values = []
	
	(hh, mm) = args[0].split(':')
	hours = (str((int(hh[1]) + 1)) + hh[0])
	if ((hh <= '05') and (mm <= (str(int(hh[1])) + hh[0])) and (hh > '00')):
	    ret_values.append(((hh + ':') + hh[::(- 1)]))
	elif (hh <= '05'):
	    ret_values.append((((hh[0] + str((int(hh[1]) + 1))) + ':') + hours))
	elif ((hh <= '09') or ((hh == '10') and (mm == '00'))):
	    ret_values.append('10:01')
	elif ((hh <= '14') and (mm < (str(int(hh[1])) + hh[0]))):
	    ret_values.append(((hh + ':') + hh[::(- 1)]))
	elif (hh <= '14'):
	    ret_values.append((((hh[0] + str((int(hh[1]) + 1))) + ':') + hours))
	elif ((hh <= '19') or ((hh == '20') and (mm <= '01'))):
	    ret_values.append('20:02')
	elif (((hh == '20') and (mm >= '02')) or ((hh == '21') and (mm < '12'))):
	    ret_values.append('21:12')
	elif (((hh == '21') and (mm >= '12')) or ((hh == '22') and (mm < '22'))):
	    ret_values.append('22:22')
	elif (((hh == '22') and (mm >= '22')) or ((hh == '23') and (mm < '32'))):
	    ret_values.append('23:32')
	elif ((hh == '00') and (mm == '00')):
	    ret_values.append('01:10')
	else:
	    ret_values.append('00:00')

	return ret_values
