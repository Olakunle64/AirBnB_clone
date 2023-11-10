#!/usr/bin/python3
""" A module that contains the State class that

defines all  attributes/methods for a state object
"""

import models.base_model

class State(models.base_model.BaseModel):
        """ a class that defines a State object that inherits from BaseModel

        Public class attributes:
        ------------------------

        name: string - empty string
        """
        name = ""
