from pydantic import BaseModel
from typing import List, Dict, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id:int
    name: int
    address : Address

class Comment(BaseModel):
    id: int
    content: str
    replies : Optional[List['Comment']] = None # this is called self replication or referancing
    # this is called forward referencing 
# incase of forward referencing , we must rebuild the class else this will not work
Comment.model_rebuild()

address  = Address(
    street="123 something",
    city="Jaipur",
    postal_code="10001"
)

user = User(
    id=1,
    name="Sourav",
    address= address
)

comment = Comment(
    id=1,
    content="First Comment",
    replies=[ 
        Comment(id=2, content= "Reply 1") ,
        Comment(id=3, content= "Reply 2") ,
        ]
)