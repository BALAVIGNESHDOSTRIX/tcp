from pydantic import BaseModel, Json
from typing import *

class ToxicInput(BaseModel):
    """ IPMITool Body Data BaseModel """
    text_data: str

    class Config:
        schema_extra = {
            "example": {
                "text_data": ""
            }
        }
        
class ToxicOutModel(BaseModel):
    value: Optional[Union[List[str], str, Dict, list, List[Dict]]] = []