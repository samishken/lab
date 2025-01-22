from flask import Blueprint, render_template, request, redirect, url_for
from models.flashcard import Flashcard
from models.database import db

# Create a blueprint
flashcards_bp = Blueprint("flashcards", __name__)

# Home route
@flashcards_bp.route("/")
def index():
    flashcards = Flashcard.query.all()
    return render_template("index.html", flashcards=flashcards)

# Add a flashcard
@flashcards_bp.route("/add", methods=["GET", "POST"])
def add_flashcard():
    if request.method == "POST":
        question = request.form.get("question")
        answer = request.form.get("answer")
        if question and answer:
            new_flashcard = Flashcard(question=question, answer=answer)
            db.session.add(new_flashcard)
            db.session.commit()
        return redirect(url_for("flashcards.index"))
    return render_template("add_flashcard.html")

# View a single flashcard
@flashcards_bp.route("/flashcard/<int:card_id>")
def view_flashcard(card_id):
    flashcard = Flashcard.query.get_or_404(card_id)
    return render_template("view_flashcard.html", card=flashcard)

# Delete a flashcard
@flashcards_bp.route("/delete/<int:card_id>", methods=["POST"])
def delete_flashcard(card_id):
    flashcard = Flashcard.query.get_or_404(card_id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect(url_for("flashcards.index"))
