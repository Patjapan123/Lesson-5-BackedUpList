class BackedUpList:
	def __init__(self,StartingValue):
		self.List=StartingValue
	def set(self,NewValue):
		self.List=NewValue
	def set_element(self,index,NewNumber):
		self.List[index]=NewNumber
	def append(self,n):
		self.List.append(n)
	def pop(self):
		self.List.remove(len(self.List)-1)
	def get(self):
		return self.List
	def get_element(self,k):
		return self.List[k]
	def backup(self):
		self.pat=self.List.copy()
	def rollback(self):
		self.List=self.pat.copy()
		def swap(self):
			