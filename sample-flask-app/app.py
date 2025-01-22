from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample flashcards data
flashcards = [
    {"question": "What is Python?", "answer": "Python is a programming language."},
    {"question": "What is Flask?", "answer": "Flask is a micro web framework for Python."},
    {"question": "What is a virtual environment?", "answer": "It is an isolated Python environment."},
]

@app.route('/')
def home():
    return render_template("home.html", flashcards=flashcards)

@app.route('/add', methods=['GET', 'POST'])
def add_flashcard():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        flashcards.append({"question": question, "answer": answer})
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/view/<int:index>')
def view_flashcard(index):
    card = flashcards[index]
    return render_template("view.html", card=card)
