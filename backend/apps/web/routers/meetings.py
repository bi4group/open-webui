from fastapi import APIRouter, Depends
from utils.utils import get_current_user

import requests

router = APIRouter()
API_URL = 'https://api.fireflies.ai/graphql'


@router.get("")
async def get_meetings(user=Depends(get_current_user)):
    auth_header = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {user.fireflies_api_key}'
    }

    data = ('{"query": "query Transcripts($userId: String) { transcripts(user_id: $userId) { title id dateString '
            'duration summary { action_items overview shorthand_bullet  } participants } }"}')

    response = requests.post(API_URL, headers=auth_header, data=data)

    return response.json()
