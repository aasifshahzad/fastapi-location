from model import Location, locations
from fastapi import HTTPException, status

def get_location_or_404(name:str)->Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No location found for {name}")
    return loc