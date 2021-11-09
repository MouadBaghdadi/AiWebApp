from fastapi import FastAPI, exceptions, Request, Response
from fastapi.responses import JSONResponse
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from .utils import request, create_token
from .settings import Settings
from .routers import google

settings = Settings()
app = FastAPI()

app.include_router(google.router)


@AuthJWT.load_config
def get_config():
    return settings


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )
