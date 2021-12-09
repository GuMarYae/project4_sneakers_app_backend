"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "SneakerController@index").name("index"),
        Get("/@id", "SneakerController@show").name("show"),
        Post("/", "SneakerController@create").name("create"),
        Put("/@id", "SneakerController@update").name("update"),
        Delete("/@id", "SneakerController@destroy").name("destroy")
    ], prefix="/sneakers", name="sneakers")
]

