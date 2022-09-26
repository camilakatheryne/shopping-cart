from src.models.product import (
    create_product,
    update_product,
    delete_product,
    get_products,
    get_product_by_code
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD de Produtos: \n1 - Create \n2 - Read  \n3 - Update \n4 - Delete \n5 - Get all items\n")
    
    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "Livro Quem Pensa Enriquece",
        "description": "O livro que mais influenciou líderes",
        "price": 32.71,
        "code": 100
    }

    if option == '1':
        # create product
        product = await create_product(
            product_collection,
            product
        )
        print(product)
    elif option == '2':
        # get product
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )
        print(product)
    elif option == '3':
        # update
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )

        product_data = {
            "price": 35.90
        }

        is_updated, numbers_updated = await update_product(
            product_collection,
            product["_id"],
            product_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )

        result = await delete_product(
            product_collection,
            product["_id"]
        )

        print(result)
    elif option == '5':
        # pagination
        products = await get_products(
            product_collection,
            skip=0,
            limit=2
        )
        print(products)

    await disconnect_db()
