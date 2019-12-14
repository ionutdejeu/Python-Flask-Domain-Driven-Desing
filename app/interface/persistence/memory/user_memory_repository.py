
from app.domain.repository.user_repository_inteface import UserRepositoryInteface
from app.domain.model.user import User

class UserMemoryRepository(UserRepositoryInteface): 
	def __init__(self,globalDataContext):
		self.data = globalDataContext
		self.data['users'] = [] #initialize the list of uwers with empty array

	def FindAll(self):
		return self.data['users'],None
	
	def FindByEmail(self, email):
		for u in self.data['users']: 
			if u.Email == email:
				return u,None
		return None,None
	
	def Save(self, user:User):
		self.data['users'].append(user)
		return user,None
	 

			
		


	