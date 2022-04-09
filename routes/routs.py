from routes.variable.registro import registro


def initAPI(app):
    app.include_router(registro)
    

