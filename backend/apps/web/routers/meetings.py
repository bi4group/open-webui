from fastapi import APIRouter, Depends

from apps.web.classes.meetings import MeetingType, MeetingService
from utils.utils import get_current_user

router = APIRouter()


@router.get("")
async def get_meetings(meeting_type: MeetingType = MeetingType.FIREFLIES, user=Depends(get_current_user)):
    return MeetingService.get_meetings(meeting_type, user)
