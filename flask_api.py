#list = [1,2,3,4,5,6]
#print(list[-4:-6:-1])

#string="Hello world"
#dict = {}
#for i in list(string):
#    if i is dict.get(i):
from flask import Flask

app = Flask(__name__)

books = [{'name' : 'Python',  'author':'Author1', 'Price':234},
{'name' : 'Java',  'author':'Author2', 'Price': 400},
{'name' : 'C#',  'author':'Author1', 'Price': 300},
{'name' : 'Go',  'author':'Author1', 'Price': 700}]

@app.route('/')
def home():
    return "<h1> First Flash App<h1>"

@app.route('/books')
def get_books():
    global books
    return {'books':books}

@app.route('/book/<name>')
def get_book(name):
    global books
    output_book =[]
    for book in books:
        if name == book['name'].lower():
            output_book.append(book)
    return {'result':output_book}

if __name__== "__main__":
    app.run(debug=True)

