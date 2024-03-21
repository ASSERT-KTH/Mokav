def func(*args):
	ret_values = []
	
	ret_values.append('CIHGANTO RWEI THHI MH!E R !'[(len(set(args[0])) % 2)::2].strip())

	return ret_values
