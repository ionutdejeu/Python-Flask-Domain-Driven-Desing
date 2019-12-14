#!flask/bin/python
from flask import Flask, request,jsonify
from app.registry.simple_dependency_container import SimpleDependencyContainer
from app.interface.service.user_flask_service import UserFlaskService
app = Flask(__name__)

#setup the global data 
#context to store values 
globalDataContex = {} 
diContainer = SimpleDependencyContainer(globalDataContex)
flaskServ = UserFlaskService(diContainer.getUseCase())

@app.route('/users', methods=['GET'])
def get_users():
    users,error = flaskServ.ListUsers()
    if error != None:
        return jsonify(error)
    return jsonify(users)

@app.route('/users', methods=['POST'])
def post_user():

    error = None
    user = None
    try:
        requestBody = request.json
        email = requestBody['email']
        if email is None:
            error = "Missing mandatory paramter"

        user,error = flaskServ.RegisterUser(email)
    except:
        error = 'Error parsing the request body'
    #mandatory parameter validation
    
    return jsonify({'data':user,
                'error':error})

if __name__ == '__main__':
    app.run()