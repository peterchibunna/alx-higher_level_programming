#!/usr/bin/python3
"""
This is the base models for all the tasks in this module
"""


class Base:
	"""
	The Base model
	"""
	__nb_objects = 0

	def __init__(self, id=None):
		"""
		We are initializing the Base object with id
		:param id:
		"""
		if id is None:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
		else:
			self.id = id
