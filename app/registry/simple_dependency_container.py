
from app.usecase.user_usecase import UserUserCase
from app.interface.persistence.memory.user_memory_repository import UserMemoryRepository
from app.domain.service.user_service import UserService
class SimpleDependencyContainer:
	useCases = []
	data = None 
	def __init__(self,globalDataContext):
		self.data = globalDataContext
		self.useCases.append({
			'name':'user-useCase',
			'build': self.newUserUseCase(self.data)
		})
	
	def newUserUseCase(self,globalDataContext):
		memRepo = UserMemoryRepository(globalDataContext)
		serv = UserService(memRepo)
		return UserUserCase(memRepo,serv)
	
	def getUseCase(self):
		return self.useCases[0]['build']
		
		
	