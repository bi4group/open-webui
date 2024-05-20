import json
import requests

from apps.web.classes.azure_active_directory import AzureActiveDirectory
from config import POWERBI_REPORT_ID, POWERBI_WORKSPACE_ID, POWERBI_CLIENT_ID, POWERBI_CLIENT_SECRET
from fastapi import HTTPException

from pydantic import BaseModel


class EmbedConfigType(BaseModel):
    reportId: str
    reportName: str
    embedUrl: str
    datasetId: str


class PowerBi:
    PBI_API_BASE = 'https://api.powerbi.com/v1.0/myorg/'

    def _get_request_header(self) -> dict[str, str]:
        """
        Get Power BI API request header

        :return dict[str, str]: Headers with the token to authorize the Power BI API call
        """
        access_token = AzureActiveDirectory.get_access_token(POWERBI_CLIENT_ID, POWERBI_CLIENT_SECRET)

        return {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}

    def get_powerbi_report_config(self) -> EmbedConfigType:
        """
        Get embed params for a report and a workspace from PowerBI API

        :returns: Report configuration from Power BY

        :raises RetrieveReportError: If report cannot be retrieved from the workspace
        """
        report_url = f'{PowerBi.PBI_API_BASE}/groups/{POWERBI_WORKSPACE_ID}/reports/{POWERBI_REPORT_ID}'
        api_response = requests.get(report_url, headers=self._get_request_header(), timeout=5)

        if api_response.status_code != 200:
            raise HTTPException(
                status_code=api_response.status_code,
                detail=f'Error retrieving report: {api_response.text}',
            )

        data = json.loads(api_response.text)

        embed_config: EmbedConfigType = {
            'reportId': data['id'],
            'reportName': data['name'],
            'embedUrl': data['embedUrl'],
            'datasetId': data['datasetId'],
        }
        return embed_config
