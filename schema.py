from marshmallow import Schema, fields

class ListSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)

class ListGetSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    age = fields.Int(dump_only=True)

class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only = True)

class ListQuerySchema(Schema):
    id = fields.Str(load_only = True)

class ListOptionalQuerySchema(Schema):
    id = fields.Str(load_only = False)

class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    
class UserQuerySchema(Schema):
    id = fields.Int(required = True)
    

class UserGetSchema(Schema):
    username = fields.Str(dump_only=True)
    password = fields.Int(dump_only=True)