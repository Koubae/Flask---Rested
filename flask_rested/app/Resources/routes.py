from flask import Flask
from flask_restful import Api
from .Product import Product


class Router:

    def __init__(self, app: Flask, api: Api, services: dict = None):
        self.app = app
        self.api = api
        self.services = services





def register_routes(api: Api) -> None:

    api.add_resource(Product, '/product/<int:product_id>')



