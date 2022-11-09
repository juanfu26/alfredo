from pydantic import BaseModel

class DataRequest(BaseModel):
    """
    Dialogflow DTO for requests

    """

    admin-area: str
    country: str
    shortcut: str
    business-name: str
    city: str
    island: str
    zip-code: str
    street-address: str
    subadmin-area: str