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

## Extend templates
If you want to extend html coding from other HTML file, you have to use the template **`{% extends 'base.html' %}`** to render.

Also, you can export and import **block of code** to render part of code.

- **`base.html`**
```html
<body>
    {% block content %}{% endblock %}
</body>
```
- **`hello.html`**
```html
{% extends 'base.html' %}
...
{% block content %} 
    {% if user_ip %}
        <h1> Hello World, my friend. Your IP is {{user_ip}} </h1>
    {% else %}
        <h1> There is not an IP </h1>
        <a href="{{url_for('index') }}">Ir al inicio</a>
    {% endif %}

    <ul>
        {% for todo in todos %}
            <li> {{todo}} </li> 
        {% endfor %}
    </ul>
{% endblock %}
...
```

### Macros
Reusable pieces of codes that let you repeat code in a lot of places on different files or templates.

- **Before using `macros`**
  - **`hello.html`**
  ```html
  {% for todo in todos %}
    <li> {{todo}} </li>
  {% endfor %}
  ```
- **After using `macros`**
  - **`macros.html`**
  ```html
  {% macro render_todo(todo) %}
    <li> {{todo}} </li> 
  {% endmacro %}
  ```
  - **`hello.html`**
  ```html
  {% import 'macros.html' as macros %}
  ...
  {% for todo in todos %}
    {{ macros.render_todo(todo) }}
  {% endfor %}
  ```