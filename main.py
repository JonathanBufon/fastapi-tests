# importar o fastapi e importar as rotas em products
from fastapi import FastAPI
from routes import products

def create_app() -> FastAPI:
    app = FastAPI(
        title="Minha API teste",
        description="API de estudos FastAPI",
        version="1.0.0",
    )

    app.include_router(products.router)
    return app

app = create_app()