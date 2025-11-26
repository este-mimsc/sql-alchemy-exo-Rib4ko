 
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    import models
    from models import User, Post

    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Flask + SQLAlchemy assignment"})

    @app.route("/users", methods=["GET", "POST"])
    def users():
        if request.method == "POST":
            data = request.get_json()
            user = User(username=data["username"])
            db.session.add(user)
            db.session.commit()
            return jsonify({"id": user.id, "username": user.username}), 201
        
        users_list = User.query.all()
        return jsonify([{"id": u.id, "username": u.username} for u in users_list]), 200

    @app.route("/posts", methods=["GET", "POST"])
    def posts():
        if request.method == "POST":
            data = request.get_json()
            user = User.query.get(data["user_id"])
            if not user:
                return jsonify({"error": "User not found"}), 400
            post = Post(title=data["title"], content=data["content"], user_id=data["user_id"])
            db.session.add(post)
            db.session.commit()
            return jsonify({"id": post.id, "title": post.title, "content": post.content, "user_id": post.user_id, "username": user.username}), 201
        
        posts_list = Post.query.all()
        return jsonify([{"id": p.id, "title": p.title, "content": p.content, "user_id": p.user_id, "username": p.user.username} for p in posts_list]), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
