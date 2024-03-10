import json
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User("George",21)
user2 = User("Mwaura",20)

#Encoding or Serialization converting python ds to json
def encoder(obj):
    if isinstance(obj,User):
        return{'Name': obj.name,'Age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('object of type user is not JSON serializable')

userJson=json.dumps(user,default=encoder)

#decoding converting json into python data structure
print(userJson)
def user_decoder(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age = dct['age'])
    return dct
user = json.loads(userJson,object_hook=user_decoder)