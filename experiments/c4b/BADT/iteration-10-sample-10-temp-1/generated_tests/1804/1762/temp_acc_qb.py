def patched_func(*args):
	global_list = []
	
	global_list.append('CIHGANTO RWEI THHI MH!E R !'[(len(set(args[0])) % 2)::2].strip())
	return global_list