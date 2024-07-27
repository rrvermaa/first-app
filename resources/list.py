from flask import request
from uuid import uuid4
from db import ListDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import ListSchema, ListGetSchema, SuccessMessageSchema, ListQuerySchema, ListOptionalQuerySchema

blp = Blueprint('Lists', __name__, description="Operations on Lists")

@blp.route('/list')
class List(MethodView):
    
    def __init__(self):
        self.db = ListDatabase()
    
    @blp.response(200, ListGetSchema(many=True))
    @blp.arguments(ListOptionalQuerySchema, location='query')
    def get(self, args):
        id = args.get('id')
        if id is None:
            return self.db.get_lists()
        else:
            result = self.db.get_list(id)
            if result == None:
                abort(404, message = "Record Doesn't exist")
            return result 
                        
                
         
    @blp.arguments(ListSchema)
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ListQuerySchema, location='query')
    def put(self, request_data, args):
        id = args.get('id')
        if self.db.update_item(id, request_data):
            return {'message': 'Data Updated successfully'}, 200
        else:    
            abort(404, message = "Data not found")

    @blp.arguments(ListSchema)
    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ListQuerySchema, location='query')
    def post(self, request_data, args):
        self.db.add_item(uuid4().hex, request_data)
        return {'message': 'List added successfully'}, 201

    @blp.response(200, SuccessMessageSchema)
    @blp.arguments(ListQuerySchema, location='query')
    def delete(self, args):
        id = args.get("id")
        if self.db.delete_item(id):
            return {"message": "Data removed"}, 200
        else:
            abort(404, message = "Not Found")
