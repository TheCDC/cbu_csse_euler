class BaseConverter:

	characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def int2wide(i):
		return BaseConverter.characters[i]

	def wide2int(c):
		return BaseConverter.characters.find(c)