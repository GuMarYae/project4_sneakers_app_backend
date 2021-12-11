""" A SneakerController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Sneaker import Sneaker

class SneakerController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", SneakerController)
        """
        id = self.request.param("id")
        return Sneaker.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index",SneakerController)
        """
        return Sneaker.all()

    def create(self):
        brand = self.request.input("brand")
        name = self.request.input("name")
        cost = self.request.input("cost")
        year = self.request.input("year")
        image = self.request.input("image")

        sneaker = Sneaker.create({"brand": brand, "name": name, "cost": cost, "year": year, "image": image})
        return sneaker

#update route
    def update(self):
        brand = self.request.input("brand")
        name = self.request.input("name")
        cost = self.request.input("cost")
        year = self.request.input("year")
        image = self.request.input("image")
        id = self.request.param("id")
        Sneaker.where("id", id).update({"brand": brand, "name": name, "cost": cost, "year": year, "image": image})
        return Sneaker.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        sneaker = Sneaker.where("id", id).get()
        Sneaker.where("id", id).delete()
        return sneaker