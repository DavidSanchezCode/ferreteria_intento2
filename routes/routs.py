from routes.variable.registro import registro
from routes.variable.login import login

def initAPI(app):
    app.include_router(registro)
    app.include_router(login)

