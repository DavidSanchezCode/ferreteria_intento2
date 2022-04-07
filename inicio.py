from fastapi import FastAPI
from routes.variable.registro import registro

app = FastAPI(
    title="proyecto personal",
    )
app.include_router(registro)

@app.get("/")
async def main_route():
    return [{"name": "david"}]