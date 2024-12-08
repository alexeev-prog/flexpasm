def get_indentation_by_level(indentation_level: int = 0):
	if indentation_level == 0:
		return ""
	else:
		return "\t" * indentation_level
