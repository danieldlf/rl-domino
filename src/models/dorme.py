from pydantic import BaseModel
from typing import List

from .stone import Stone

class Dorme(BaseModel):
    sleeping_stones: List[Stone]