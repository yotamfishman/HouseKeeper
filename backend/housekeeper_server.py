from flask import Flask, jsonify, send_from_directory, request, redirect, url_for, abort, make_response
from flask_pymongo import PyMongo
from flask_login import LoginManager, mixins, login_user, login_required, logout_user

app= Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

app.secret_key = b'\xd2\xf2\n\xbd\x0c*#\xbf\xad\x12\x86\x89\xee\x866~'

mongo.db.users.delete_many({})
mongo.db.users.insert_one({
    "_id": "0",
    "name": "yotam",
    "passwd": "1234"
})

class User (mixins.UserMixin):
    def __init__(self, name: str, user_id, passwd: str):
        self.name = name
        self.id = user_id
        self.passwd = passwd


@login_manager.user_loader
def load_user(usr_id):
    user = mongo.db.users.find_one({"_id": usr_id})
    if user is None:
        return None
    return User(user["name"], user["_id"], user["passwd"])


mongo.db.chores.delete_many({})
mongo.db.chores.insert_one( {
            "title": "Take out the trash",
            "description": "Take the trash out from the can",
            "icon": "/icons/trash.svg",
            "duration": "4 minutes",
            })
mongo.db.chores.insert_one( {
            "title": "Wash the dishes",
            "description": "wash all the dishes in the sinks",
            "icon": "/icons/sink.svg",
            "duration": "30 minutes",
            })
mongo.db.chores.insert_one( {
            "title": "Water the plants",
            "description": "Make sure to water to water the plants in the living roo as well",
            "icon": "/icons/leaf.svg",
            "duration": "10 minutes",
            })


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/')
@app.route('/add')
@login_required
def index():
    return send_from_directory('../frontend/dist', 'index.html')

@app.route('/login', methods=['GET'])
def login():
    return send_from_directory('../frontend/dist/auth', 'index.html')
    
@app.route('/login', methods=['POST'])
def login_post():
    name = request.json["name"]
    passwd = request.json["passwd"]
    user_data = mongo.db.users.find_one({"name": name})
    if passwd != user_data["passwd"]:
        abort(401)
    
    logout_user()
    login_user(User(name, user_data["_id"], passwd))
    return make_response('OK')

@app.route('/add', methods = ['POST'])
@login_required
def add():
    chore = request.json
    mongo.db.chores.insert_one(chore)
    return make_response('OK')


@app.route('/my-chores.json')
@login_required
def my_choures_json():
    chorse = [chore for chore in mongo.db.chores.find()]
    for chore in chorse:
        chore.pop("_id")
    return jsonify(chorse)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return make_response('OK')

@app.route('/<path:path>')
def serve_static(path: str):
    return send_from_directory('../frontend/dist', path)


app.run()