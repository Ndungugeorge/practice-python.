
import uuid
from datetime import datetime

class BaseModel:

    def __init__(self,*args,**kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict

    def __str__(self) -> str:
        class__name = self.__class__.__name__
        return "[{}] [{}] [{}]".format(class__name,self.id,self.__dict__)