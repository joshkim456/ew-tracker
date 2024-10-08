from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    rows = db.get_ews()
    return render_template('list.html', ews=rows)

@app.route('/add', methods=['POST'])
def add_ew():
    task = request.form['task']
    subject = request.form['subject']
    beak = request.form['beak']
    dueDate = request.form['dueDate']

    db.create_ew(task, subject, beak, dueDate)

    return redirect('/')


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass