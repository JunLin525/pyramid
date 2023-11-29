from pyramid.view import (
    view_config,
    view_defaults
    )



# First view, available at http://localhost:6543/
@view_defaults(renderer = 'home.pt')
class TutorialViews:
    def __init__(self,request):
        self.request=request

    # /howdy
    @view_config(route_name='home')
    def home(self):
        return {'name': 'HomeView'}
    def hello(self):
        return {'name': 'Hello world'}