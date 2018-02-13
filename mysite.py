from flask import Flask, request
from flask import render_template

app = Flask(__name__)





# Root link ===================================================================

welcomes = ["welcome", "language2", "language3"]
    
@app.route("/")
def hello():
    return render_template('index.html', data = welcomes, books_data = books)
    



# Books link ===================================================================
    
books = [
    {'title': 'The sky', 'author': 'Dan'},
    {'title': 'What is this', 'author': 'Danutz'},
    {'title': 'Just a title', 'author': 'DumiD'},]
    
@app.route("/books", methods=['GET', 'POST'])
def booksFunction():
    if request.method == "POST":
        
        # This is what the user types
        title = request.form.get('title')
        author = request.form.get('author')
        books.append({'title': title, 'author': author})
        
    return render_template('books.html', books_data = books)







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

