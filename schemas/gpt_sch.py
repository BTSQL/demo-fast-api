
from pydantic import BaseModel


class GptRequestSch(BaseModel):
    title_nm: str

    class Config :
        orm_mode = True
        schema_extra = {
            "example": {
                "title_nm": "Base Tesla Model 3 Inventory has $2,410 discount and now Qualifies for $7,500 Tax Credit"
            }
        }

class GptResponseSch(BaseModel):
    bard_msg_ctt: str
    openai_msg_ctt: str
    kakao_msg_ctt: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "bard 메시지 내용 입니다",
                "openai 메시지 내용 입니다",
                "kakao 메시지 내용 입니다"
            }
        }
