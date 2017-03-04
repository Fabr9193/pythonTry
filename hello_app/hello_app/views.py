from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'greetings myself'}

@view_config(route_name='myTest', renderer='templates/myowntemplate.jinja2')
def my_ajax_view(request):
    return {'project' : "this is a test", 
            'anotherOne' : "another test" }