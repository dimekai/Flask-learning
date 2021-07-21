from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')
def index():
    # Gettin IP user who starts the app
    user_ip = request.remote_addr

    # Redirect a new route
    response = make_response(redirect('/hello'))

    # Setting a cookie using IP user
    response.set_cookie('cookie_user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('cookie_user_ip')
    context = {
          'user_ip' : user_ip
        , 'todos'   : todos
    }
    return render_template('hello.html', **context)
    #return f'Hello, world baby, your IP is {user_ip} using a cookie'







