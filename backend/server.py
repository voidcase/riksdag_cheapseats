from flask import Flask
from routes.topics import topics_bp
from routes.annotations import annotations_bp
<<<<<<< HEAD
#import gunicorn # token import
=======
from routes.debate import debate_bp
import gunicorn # token import
>>>>>>> 96b8b4ba626249791d9669669e4fa0511d4ea7e9

app = Flask(__name__)
app.register_blueprint(topics_bp)
app.register_blueprint(annotations_bp)
app.register_blueprint(debate_bp)

if __name__ == '__main__':
    app.run(debug=True)
