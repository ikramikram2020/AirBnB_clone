#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
class BaseModel;
    """Represents the BaseModel of the HBnB project."""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

=======
import sys
import uuid
from datetime import datetime
import models

sys.path.append('..')


class BaseModel:
    """Parent/base class. All other classes inherits from here."""

    def __init__(self, *_args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A method to save attributes of an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """hadles the key-paired values to dictionary

        Returns:
            dict: return dictionary
        """
        cls_dict = {'__class__': self.__class__.__name__}
        cls_dict.update({k: v.isoformat()
                        if isinstance(v, datetime)
                        else v for k, v in self.__dict__.items()})
        return cls_dict
>>>>>>> 728acc1ead0baf0c32c34638bf965fedc88afd23
