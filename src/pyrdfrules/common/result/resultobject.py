
from typing import Protocol
from pydantic import BaseModel, ValidationError
import json
from traceback import TracebackException
from typing import no_type_check, Type, Any

class ResultObject(BaseModel):
    """Base result object class.

    Attributes:
        extra (dict): Extra attributes, which were not mapped to the model.
    """
    
    extra: dict = {}
    
    def __init(self, **data):
        try:
            super().__init__(**data)
        except ValidationError as e:
            self.extra = data            
        pass
    
    @classmethod
    def create(cls, data: dict, model: Type[BaseModel]):
        """Creates a new ResultObject instance from a dictionary.
        
        Args:
            data (dict): Dictionary with data.
            model (Type[BaseModel]): Pydantic model class.
        
        Returns:
            ResultObject: ResultObject instance.
        """
        
        try:
            return model(**data)
        except ValidationError as e:
            return ResultObject(**data)
        pass