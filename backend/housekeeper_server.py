from flask import Flask, jsonify, send_from_directory, request, redirect, url_for, abort, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .chores import Chore
from .data_base_manager import DbManager

app= Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = b'\xd2\xf2\n\xbd\x0c*#\xbf\xad\x12\x86\x89\xee\x866~'
DbManager.init(app)

DbManager.users.clear_all()
DbManager.users.add_user("Yotam", "1234")


@login_manager.user_loader
def load_user(usr_id):
    return DbManager.users.get_user_by_id(usr_id)


DbManager.chores.clear_all()
DbManager.chores.add_chore(Chore("Take out the trash", "Take the trash out from the can", "/icons/trash.svg", "4 minutes", current_user.id))
DbManager.chores.add_chore(Chore("Wash the dishes", "wash all the dishes in the sinks", "/icons/sink.svg", "30 minutes", current_user.id))
DbManager.chores.add_chore(Chore("Water the plants", "Make sure to water to water the plants in the living roo as well", "/icons/leaf.svg", "10 minutes", current_user.id))


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
    user = DbManager.users.get_user_by_name(name)
    if user is None or passwd != user.passwd:
        abort(401)
    
    logout_user()
    login_user(user)
    return make_response('OK')

@app.route('/add', methods = ['POST'])
@login_required
def add():
    chore = request.json
    DbManager.chores.add_chore(Chore.create(chore))
    return make_response('OK')


@app.route('/my-chores.json')
@login_required
def my_choures_json():
    chorse = [chore.json for chore in DbManager.chores.get_all_chores()]
    return jsonify(chorse)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return make_response('OK')

@app.route('/username.json')
@login_required
def user_json():
    user = load_user(current_user.id)
    return jsonify({"username": user.name})

@app.route('/<path:path>')
def serve_static(path: str):
    return send_from_directory('../frontend/dist', path)

if __name__ == "__main__":
    app.run()