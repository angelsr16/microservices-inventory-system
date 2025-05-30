from fastapi import FastAPI
from api.v1 import auth
from mangum import Mangum

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Auth"])


@app.get("/users")
async def root():
    return {"msg": "Hello from auth service"}


asgi_handler = Mangum(app)


def handler(event, context):
    # 🔍 Check for API Gateway v1 or v2 (HTTP)
    if "httpMethod" in event or (
        event.get("version") == "2.0" and "requestContext" in event
    ):
        return asgi_handler(event, context)
