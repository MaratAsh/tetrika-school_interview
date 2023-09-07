def strict(func):
	annotations = list(func.__annotations__.keys())
	pos_arg_count = len(annotations) - 1 \
		if 'return' in annotations \
		else len(annotations)
	def decorator(*args):
		if (len(args) != pos_arg_count):
			return TypeError
		for arg_id in range(len(args)):
			if type(args[arg_id]) != func.__annotations__[annotations[arg_id]]:
				return TypeError
		return func(*args)
	return decorator
