from flask import Flask, jsonify, send_from_directory
from flask_pymongo import PyMongo

app= Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

mongo.db.chores.delete_many({})
mongo.db.books.insert_one({'title': "todo title", 'body': "todo body"})


@app.route('/')
def index():
    return send_from_directory('../frontend/dist', 'index.html')

@app.route('/add')
def add():
    return send_from_directory('../frontend/dist', 'index.html')

@app.route('/my-chores.json')
def my_choures_json():
    return jsonify([chore for chore in mongo.db.chores.find()])

@app.route('/<path:path>')
def serve_static(path: str):
    return send_from_directory('../frontend/dist', path)


app.run()