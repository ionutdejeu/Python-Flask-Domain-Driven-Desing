from app.domain.model.user import User
from app.usecase.user_usecase import UserUserCase,UserUseCaseInteface
from flask import jsonify

#wrapper class over the business use case 
class UserFlaskService:
    useCase:UserUseCaseInteface=None
    def __init__(self,usecase:UserUseCaseInteface):
        self.useCase = usecase

    def ListUsers(self):
        users,error = self.useCase.ListUsers()
        if error != None:
            return None,error
        usersDao = []
        for u in users:
            usersDao.append(self.UserBusinessObjectToDAO(u))
        return usersDao,error
    
    def RegisterUser(self,email):
        user,error = self.useCase.RegisterUser(email)
        if error != None:
            return None,error
        return self.UserBusinessObjectToDAO(user),error
    
    def UserBusinessObjectToDAO(self,userBusinessObject:User):
        dao = {}
        dao['Id'] = userBusinessObject.Id
        dao['Email'] = userBusinessObject.Email
        return dao

    