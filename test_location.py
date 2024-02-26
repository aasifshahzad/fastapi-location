from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from location import app
from depend import get_location_or_404
from model import Location

locations = {
    "zeeshan": Location(name="Zeeshan", location="Karachi"),
    "javed": Location(name="Javed", location="Lahore"),
}

def fake_get_location_or_404(name: str) -> Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found for {name}")
    return loc


app.dependency_overrides[get_location_or_404] = fake_get_location_or_404

client = TestClient(app)
print(client)
    
def test_read_location():
    response = client.get("location/zia")
    assert response.status_code == 200
    assert response.json() == {"name": "Zia", "location": "Karachi"}
    # assert response.status_code == status.HTTP_404_NOT_FOUND

    
    
def test_location_404():
    response = client.get("/location/javed")
    assert response.status_code == status.HTTP_404_NOT_FOUND