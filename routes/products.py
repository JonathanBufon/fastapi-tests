## rotas de produtos, importar o router do fastapi e o BaseModel da biblioteca Pydantic
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


class Product(BaseModel):
    name: str
    price: float
    is_offer: bool = False

produtos_criados: list[Product] = []

@router.get("/")
def list_products():
    return {
        "products": produtos_criados
    }

@router.post("/")
def create_product(product_send: Product):
    produtos_criados.append(product_send)
    return {
        "message": "Produto criado com sucesso",
        "product": product_send
    }