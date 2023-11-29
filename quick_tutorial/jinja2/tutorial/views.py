from pyramid.view import (
    view_config,
    view_defaults
    )



# First view, available at http://localhost:6543/
@view_defaults(renderer = 'home.jinja2')
class TutorialViews:
    def __init__(self,request):
        self.request=request

    # /howdy
    @view_config(route_name='home')
    def home(self):
        return {'name': 'HomeView'}
    @view_config(route_name='hello')
    def hello(self):
        return{'name':'hello view'}