# From Bottle IMPORT The Most Important Functions
from bottle import route,run,template

# Make A Decorator Call @ROUTE For Special URL
# Also Pass A Variable NAME IN The Address
@route('/hello/<name>')
# Now We Define Main Page OF Routing Above Called Index
# And We Pass Name Variable Into Function
def index(name):
	# We Also USE Bottle Template Engin To Return HTML With {{Var}}
    return template('<b>Hello {{name}}</b>!', name=name)

# After All We Run The Server
run(host='localhost', port=8080)

####################################################

from bottle import get, post, request # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

#######################################################