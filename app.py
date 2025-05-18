from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-key'

# --- Part 1: static JSON API --- ssgit checkout master_1s
@app.route('/api')
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)


app.config["MONGO_URI"] = "mongodb+srv://honey:999026264a@cluster0.hvfslcb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        doc = request.form.to_dict()
        try:
            mongo.db.users.insert_one(doc)
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"Error: {e}")
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
