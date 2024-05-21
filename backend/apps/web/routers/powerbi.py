import logging

from fastapi import Response, Request, APIRouter

from apps.web.classes.powerbi import PowerBi, EmbedConfigType
from config import SRC_LOG_LEVELS, POWERBI_REPORT_ID, POWERBI_WORKSPACE_ID

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["POWERBI"])

router = APIRouter()


@router.get("/embed-config", response_model=EmbedConfigType)
async def get_powerbi_embed_config():
    return PowerBi().get_powerbi_report_config()
