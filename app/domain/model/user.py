import json

class User:
	Id=None
	Email=None
	def __init__(self,id,email):
		super().__init__()
		self.Id=id
		self.Email = email
	
	def getID(self):
		return self.Id

	def getEmail(self):
		return self.Email

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)