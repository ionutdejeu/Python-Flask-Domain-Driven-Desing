from app.domain.repository.user_repository_inteface import UserRepositoryInteface

class UserService:
	userRepository:UserRepositoryInteface=None
	def __init__(self,user_repository:UserRepositoryInteface):
		self.userRepository = user_repository
		super().__init__()

	def Duplicated(self,email):
		user,error = self.userRepository.FindByEmail(email)
		if user != None:
			return None,email+ "already exixts "
		if error != None:
			return None,error
		return None,None
	