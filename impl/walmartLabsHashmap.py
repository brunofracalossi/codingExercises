class hashmap:

	def __init__(self):
		self.hashmap = {}

	def insert(self, value, word):
		if value in self.hashmap:
			temp = self.hashmap[value]
			temp.append(word)
			self.hashmap[value] = temp
		else:
			self.hashmap[value] = []
			self.hashmap[value].append(word)

		return self.hashmap

	def findAndReplace(self, old, new):
		for i in self.hashmap:
			my_str = self.hashmap[i]
			my_str = [w.replace(old,new) for w in my_str]
			self.hashmap[i] = my_str

		return self.hashmap

	def empty_hashmap(self):
		self.hashmap.clear()

	def get_hashmap(self):
		return self.hashmap