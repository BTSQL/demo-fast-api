from fastapi import APIRouter
from schemas.comm_sch import EmailSendRequestSch
from apis.utils.utils import send_email

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "hello world"}


@router.post("/send_email")
async def send_email_router(info: EmailSendRequestSch):
    print(EmailSendRequestSch)
    send_email(info.user_email, info.title,  info.content)
    return True

