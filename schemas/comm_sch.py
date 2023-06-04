
from pydantic import BaseModel, EmailStr
from typing import Optional


class EmailSendRequestSch(BaseModel):
    user_email : EmailStr
    title : str
    content : Optional[str]

    class Config : 
        orm_mode = True
        schema_extra = {
            "example": {
                "user_email": "baezzang@sk.com",
                "title": "반갑습니다",
                "content": "데브오션에서 만나게 되어 반갑습니다",
            }
        }
