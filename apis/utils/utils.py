
from optparse import Option
from pydantic import EmailStr
from config.config import settings
from typing import Optional

import requests

def send_email(mail_address : EmailStr, title :str, content: Optional[str]):
    
    res =  requests.post(
        "https://api.mailgun.net/v3/petmit.org/messages",
        auth=("api", settings.EMAIL_API_KEY),
        data={
            "from": "펫밋관리자 <mailgun@petmit.org>",
            "to": [mail_address],
            "subject": title,
            "text": content,
            # "text": "아래 링크를 클릭하면 회원가입 인증이 완료됩니다. \n" + url,
        },
    )

    print(res.status_code)

    if res.status_code == 200:
        print("메일발송 성공 되었습니다")
        return True


    return False