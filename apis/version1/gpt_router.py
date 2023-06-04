from fastapi import APIRouter
from schemas.gpt_sch import GptRequestSch, GptResponseSch
from kakaotrans import Translator
from bardapi import Bard
from config.config import settings
import openai, json, requests

router = APIRouter()
translator = Translator()


@router.post("/translate/by/gpt", response_model= GptResponseSch)
async def translate_by_gpt_router(req: GptRequestSch):

    openai_result = await translate_by_openai(req)
    bard_result = await translate_by_bard(req)
    kakao_result = await translate_by_kakao(req)

    return {
        "bard_msg_ctt": bard_result,
        "openai_msg_ctt": openai_result,
        "kakao_msg_ctt": kakao_result,
    }

async def translate_by_openai(req: GptRequestSch) :
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user',
                      'content': req.title_nm + '한국어로 100자 이내로 설명해줘'}],
        'temperature': 0.3,
        'max_tokens': 150,

    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=settings.OPENAI_HEADERS, json=data)
    output = json.loads(response.text)
    openai_result = output["choices"][0]["message"]["content"]

    return openai_result

async def translate_by_bard(req: GptRequestSch) :
    bard = Bard(token=settings.BARD_API_KEY)
    bard_result = bard.get_answer(req.title_nm + '한국어로 100자 이내로 설명해줘')['content']
    return bard_result

async def translate_by_kakao(req: GptRequestSch) :
    kakao_result = translator.translate(req.title_nm, src='en', tgt='kr')
    return kakao_result