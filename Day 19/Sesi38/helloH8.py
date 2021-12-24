from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def hello_world():    
#     return 'Hello, World!'

# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):    
#     return f"Hello, {escape(name)}!"

@app.route('/shop')
@app.route('/')
def index():
# def index(pageName):
    # html = 'Hello HTML'
    # html += f'This is {pageName}'  
    # return html  
    return 'Index Page'

@app.route('/<pageName>')
def functionPageName(pageName):
    html = 'Hello HTML'
    html += f'<h2> This is {escape(pageName)}</h2>'  
    return html 

# @app.route('/hello')
# def hello():    
#     return 'Hello, World (Page => hello)'        



@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'

#STATIC FILES
# url_for('static', filename='style.css')

# LOGIN
# from flask import request
# @app.route('/login', methods=['GET', 'POST'])
# def login():    
#     if request.method == 'POST':        
#         return do_the_login()    
#     else:        
#         return show_the_login_form()

#RENDERING TEMPLATE
# from flask import render_template
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):    
#     return render_template('hello.html', name=name)

if __name__ == '__main__':    
    app.run()
