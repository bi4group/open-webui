import msal

from cachetools import TTLCache
from config import AZURE_TENANT_ID


class AzureActiveDirectory(object):
    """
    Azure Active Directory class

    Manages the connectivity with Active Directory to authenticate users / service principals
    """

    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

    """
    Tokens are cached to improve performance and avoid unnecessary requests to Azure Active Directory
    Azure AD default expiration time is 3599 (~1h), so we use in memory cache with TTL=3000s
    It's simple and effective, but each container/gunicorn worker has its own cache
    If we ever need to implement a centralized cache, use it for this also, but not worth at this point
    """
    TOKEN_CACHE = TTLCache(maxsize=1, ttl=3000)

    @classmethod
    def get_access_token(cls, client_id: str, client_secret: str) -> str:
        """
        Get an Access token to interact with the Power BI API scope

        :return: str The access token
        """
        cached_token = cls.TOKEN_CACHE.get('access_token')
        if cached_token:
            return cached_token

        # There's no token, or it has expired, generate a new one a store it
        new_token = cls.get_fresh_access_token(client_id, client_secret)
        cls.TOKEN_CACHE['access_token'] = new_token

        return new_token

    @classmethod
    def get_fresh_access_token(cls, client_id: str, client_secret: str) -> str:
        """
        Generates and returns an Access token to interact with the Power BI API scope

        :return: str The access token
        """

        authority = f'https://login.microsoftonline.com/{AZURE_TENANT_ID}'
        clientapp = msal.ConfidentialClientApplication(client_id, client_credential=client_secret, authority=authority)

        # Make a client call if Access token is not available in cache
        response = clientapp.acquire_token_for_client(scopes=cls.SCOPE)
        return response['access_token']
