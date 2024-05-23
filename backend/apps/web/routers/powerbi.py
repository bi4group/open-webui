from fastapi import APIRouter

from apps.web.classes.powerbi import PowerBi, EmbedConfigType

router = APIRouter()


@router.get("/embed-config", response_model=EmbedConfigType)
async def get_powerbi_embed_config():
    return PowerBi().get_powerbi_report_config()
