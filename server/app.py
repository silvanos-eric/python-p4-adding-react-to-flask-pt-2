from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import Movie, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
Migrate(app, db)


@app.route('/movies', methods=['GET'])
def movies():
    if request.method == 'GET':
        movie_list = Movie.query.all()
        movie_dict_list = [movie.to_dict() for movie in movie_list]
        return movie_dict_list


if __name__ == '__main__':
    app.run(port=5555)
