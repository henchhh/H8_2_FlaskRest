from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is the home page</h1>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    age = 90
    pets = ['cat', 'dog', 'bird', 'fish'] #list
    petDict = {'cat':'nameCat', 'dog':'nameDog', 'bird':'nameBird', 'fish':'nameFish'} #dictionary   
    return render_template('hello.html', tempName=name, tempAge=age, tempPets=pets, tempPetDict=petDict)

if __name__ == '__main__':    
    app.run(debug=True)        