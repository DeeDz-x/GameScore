import configparser
import jwt
SECRET_KEY = "NIckUFjZseVKY05IQSnBrJRiELQWVKTMZlGdAWutNbTf3X9oDBAYE4L2RyUH7MOqx8w6PHFg1GCpmSO"

def encode(user_id):
    return jwt.encode({"user_id":user_id},SECRET_KEY,algorithm="HS256")

def decode(token):
    return jwt.decode(str.split(token)[1],SECRET_KEY,algorithms="HS256")["user_id"]