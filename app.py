from flask import Flask, render_template, request
from functions import add_expense
from file_handler import read_expense
from exception_handler import validate

app = Flask(__name__)

@app.route('/')
def home():
    data = read_expense()
    return render_template("index.html", data=data)

@app.route('/add', methods=['POST'])
def add():
    amount = request.form['amount']
    category = request.form['category']

    if not validate(amount):
        return "Invalid amount"

    add_expense(amount, category)
    return home()

if __name__ == "__main__":
    app.run(debug=True)