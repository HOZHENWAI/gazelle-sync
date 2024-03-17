"""
Client object to navigate.
https://redacted.ch/wiki.php?action=article&id=455
"""
import warnings
from typing import Optional, Dict

import requests
import aiohttp
from structlog import get_logger


logger = get_logger(__name__)


class RedactedClient:
    """A redacted client that is necessary to perform intend operation.
    We are required to get downloaded torrent/uploaded torrent.
    We have to be able to then search for torrent downloaded from another client...
    And finally, if required we have to be able to create new torrent and upload
    using the information of the other torrent.
    To finish upload, we would also require to be able to download torrent
    Must also define rate limit, etc...
    """

    URL: str = "https://redacted.ch/ajax.php"
    HEADERS = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept-Charset': 'utf-8',
        'User-Agent': 'test-agent'
    }

    # HARDCODED RATELIMIT, CHANGE THIS AT YOUR OWN RISK
    STANDARD_RATE_LIMIT: int = 5 # per 10 sec
    API_RATE_LIMIT: int = 10 # per 10 sec

    def __init__(self,
                 asynchronous: bool = False,
                 api_key: Optional[str] = None,
                 session_token: Optional[str] = None,
                 login: Optional[str] = None,
                 password: Optional[str] = None,

                 ):
        """If api key is provided, then login and password are not used.
        Optionally, the session token is used.
        Otherwise, the login and password are used to get the key.
        """
        self.asynchronous = asynchronous
        self.api_key = api_key
        self.session_token = session_token
        self.login = login
        self.password = password

        if (login is not None) or (session_token is not None):
            warnings.warn("You have chosen to use the login to authenticate against Redacted. "
                          "Verify that you are not using 2FA.")

        self.reload_session()


    def reload_session(self) -> None:
        """"""
        if self.asynchronous is False:
            self.session = requests.session()
        else:
            self.session = aiohttp.ClientSession()


    def _sync_get_snatched(self) -> Dict:
        """"""
        with self.session.get()

    # def login(self):
    #     """Try to login"""
