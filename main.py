from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from settings import Settings
from routers import google
from models.database import Base, engine

settings = Settings()
app = FastAPI()

app.include_router(google.router)

Base.metadata.create_all(bind=engine)


@AuthJWT.load_config
def get_config():
    return settings


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )

# register_tortoise(
#     app,
#     db_url='sqlite://test.sqlite3',
#     modules={"models": ["models.user"]},
#     generate_schemas=True,
#     add_exception_handlers=True
# )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)