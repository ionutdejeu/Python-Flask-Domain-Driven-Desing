from app.domain.model.user import User
from app.domain.repository.user_repository_inteface import UserRepositoryInteface
from app.domain.service.user_service import UserService

class UserUseCaseInteface: 
    def ListUsers(self):
        pass
    def RegisterUser(self,user:User):
        pass

class UserUserCase(UserUseCaseInteface): 
    repository:UserRepositoryInteface = None
    service:UserService = None
    
    def __init__(self,repository,service):
        self.repository = repository
        self.service = service

    def ListUsers(self):
        users, error = self.repository.FindAll()
        if(error!= None):
            return None,error
        return users,None
    def RegisterUser(self,pEmail):
        uid = "1234"
        user,error = self.service.Duplicated(pEmail)
        if error != None:
            return None,error
        newUser = User(uid,pEmail)
        savedUser,error = self.repository.Save(newUser)
        if error != None: 
            return error
        return savedUser,None
    
    
