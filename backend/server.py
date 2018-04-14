from flask import Flask
from routes.topics import topics_bp
from routes.annotations import annotaions_bp
import gunicorn # token import

app = Flask(__name__)
app.register_blueprint(topics_bp)
app.register_blueprint(annotaions_bp)

if __name__ == '__main__':
    app.run(debug=True)
