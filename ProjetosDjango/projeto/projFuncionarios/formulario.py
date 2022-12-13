from bottle import route, run, request

@route('/', method='GET')
def index_get():
    return """
        <form action="/" method="post">
            <label>Username:</label>
            <input name="username" type="text" /></br>

            <label>Password:</label>
            <input name="password" type="password" /></br>

            <input value="Login" type="submit" />
        </form>
    """

@route('/', method='POST')
def index_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return f"""
        <h1>Suas informações</h1>
        </br>
        <h4>{username}</h4>
        <h4>{password}</h4>
    """

run(port=8080)

