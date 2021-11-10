from pydantic import BaseSettings
import datetime


class Settings(BaseSettings):
    APP_ENV: str = 'dev'
    GOOGLE_CLIENT_ID: str
    GOOGLE_SECRET: str
    GOOGLE_URL: str = None
    SECRET: str
    authjwt_secret_key: str
    authjwt_token_location: set = {'cookies'}
    authjwt_cookie_csrf_protect: bool = False

    class Config:
        env_file = 'dev.env'
