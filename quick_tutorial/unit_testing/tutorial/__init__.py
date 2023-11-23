from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('\
                    <title>hello</title>\
                    <body><h2>wow</h2><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/hello/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()