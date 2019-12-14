
from app.domain.model.user import User
class UserRepositoryInteface:
    def FindAll(self):
        pass
    def FindByEmail(self,email):
        pass
    def Save(self,user:User):
        pass
