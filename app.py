from flask import Flask
from resources.list import blp as ListBluePrint 
from resources.user import blp as UserBluePrint 
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import Blocklist
# from flask_jwt_extended import 
app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Items Rest Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config['JWT_SECRET_KEY'] = "1029232569986661428033657078043058482"

api = Api(app)

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_blocklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in Blocklist

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        {
            "description": "user has been logout",
            "error": "token_revoked"
        },
        401
    )
    


api.register_blueprint(ListBluePrint)
api.register_blueprint(UserBluePrint)






