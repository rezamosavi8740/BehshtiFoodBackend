from fastapi import FastAPI
from Authentication.loginAPIS import Login

app = FastAPI()

app.include_router(Login)

# @app.get('/')
# async def first_api():
#     return 'firstapi'