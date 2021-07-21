# Flask-learning
Repository to learn flask


- Enviroment variables to run flask:
  - `export FLASK_APP=main.py`
  - `export FLASK_DEBUG=1`

- Run flask
  - `flask run`


## Template
- Let you render static and dynamic information in a web app, and you can pass variables.
  - `{{name_variable}}`

- To use this template you have tu import `render_template` function
- If you want to pass one or more variables you can **extend a dictionary**:
  ```python
  user_ip = request.cookies.get('cookie_user_ip')
    context = {
          'user_ip' : user_ip
        , 'todos'   : todos
    }
    return render_template('hello.html', **context)
  ```

### Structures Control
- Structure conditional **`if-else`**
  ```html
  {% if user_ip %}
        <h1> Hello World, my friend. Your IP is {{user_ip}} </h1>
  {% else %}
        <h1> There is not an IP </h1>
        <a href="{{url_for('index') }}">Ir al inicio</a>
  {% endif %}
  ```
- Loop structure: **`for`**
  ```html
  <ul>
    {% for todo in todos %}
      <li> {{todo}} </li> 
    {% endfor %}
  </ul>
  ```