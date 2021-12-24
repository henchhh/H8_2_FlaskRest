from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is the home page</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return doTheLogin()    
    else:        
        return showTheLoginForm()

def doTheLogin():
    return f'Do the login with HTTP Request Method : {request.method}'        

def showTheLoginForm():
    return f'Show the login form with HTTP Request Method : {request.method} <br> and this is the login form'

if __name__ == '__main__':    
    app.run()        