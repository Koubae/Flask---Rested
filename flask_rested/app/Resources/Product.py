from flask_restful import Resource


class Product(Resource):

    def get(self, product_id: int) -> dict:
        return {"GET": True}

    def post(self) -> dict:
        return {"POST": True}

    def put(self, product_id: int) -> dict:
        return {"PUT": True}

    def patch(self, product_id: int) -> dict:
        return {"PATCH": True}

    def delete(self) -> dict:
        return {"DELETE": True}
