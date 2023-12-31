from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/howdy/{first}/{last}/{number}')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()