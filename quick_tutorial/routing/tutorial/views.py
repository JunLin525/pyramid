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
        first = self.request.matchdict['first']
        last  = self.request.matchdict['last']
        number = self.request.matchdict['number']
        return {'name': 'HomeView',
                'first': first,
                'last': last,
                'number':number
        }

