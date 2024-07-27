import uuid
from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blurprint, abort
from schema import UserSchema, UserQuerySchema

blp = Blurprint('Users', __name__, description ="operations on Users")

@blp.route('/users')
class User(MethodView):
    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.response(UserQuerySchema, location = "query")
    def get(self,args):
        id = args.get('id')
        result = self.db.get_item(id)
        if result in None:
            abort(404, message="User Doesn't exist")
        return result
        
    # @blp.arguments()
    # @blp.response(200, )
    # def post(self,request_data):
    #     id = uuid.uuid4().hex
    #     self.db.add_user(id,request_data)
        
    # @blp.response(200, ItemGetSchema(many=True))
    # @blp.response(ItemOptionalQuerySchema, location = "query")
    # def get(self,args):
    #     id = args.get('id')
    #     if id in None:
    #         return self.db.get_item()
    #     else:
    #         result = self.db.get_item(id)
    #         if result in None:
    #             abort(404, message="Record Dpesn't exist")
    #         return result
        
    

    
