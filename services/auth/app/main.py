from fastapi import FastAPI
from api.v1 import auth
from mangum import Mangum

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

handler = Mangum(app)
