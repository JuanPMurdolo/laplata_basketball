from flask import Flask
from routes.players import players_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(players_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)