from pydantic import BaseModel

class Location(BaseModel):
    name: str
    location:str
    
locations = {
    "zia" : Location(name="zia", location="Karachi"),
    "ali" : Location(name="ali", location="Lahore"),
}