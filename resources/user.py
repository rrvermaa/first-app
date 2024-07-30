import uuid
from db.users import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import UserSchema, UserQuerySchema, SuccessMessageSchema
import hashlib
from flask_jwt_extended import create_access_token, jwt_required, get_jwt 
from blocklist import Blocklist

blp = Blueprint('Users', __name__, description ="operations on Users")

@blp.route('/login')
class Login(MethodView):
    def __init__(self):
        self.db = UserDatabase()
    
    @blp.arguments(UserSchema)
    def post(self, request_data):
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode('utf-8')).hexdigest()
        
        user_id = self.db.verify_user(username, password)
        if user_id:
            return {"access_token":create_access_token(identity=user_id)}
        abort(403, message='Username or password not correct')

@blp.route('/logout')
class Logout(MethodView):
    
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        Blocklist.add(jti)
        return {"message": "user logout"}


@blp.route('/users')
class User(MethodView):
    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerySchema, location = "query")
    def get(self,args):
        id = args.get('id')
        result = self.db.get_user(id)
        print(result)
        if result is None:
            abort(404, message="User Doesn't exist")
        return result
        
    
    @blp.arguments(UserSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        #  check if aready exist
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode('utf-8')).hexdigest()

        if self.db.add_user(username, password):
            return {'message': 'List added successfully'}, 201
        abort(403, message="User already exist")
        
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(UserQuerySchema, location='query')
    def delete(self, args):
        id = args.get("id")
        if self.db.delete_user(id):
            return {"message": "User removed"}, 200
        else:
            abort(404, message = "User Not Found")


    
