from flask import Flask
from app.routes import bp as routes_blueprint

# Create the Flask app instance
app = Flask(__name__)

# Register the routes blueprint
app.register_blueprint(routes_blueprint)

# Set the environment variable for development or production
app.config['ENV'] = 'development' 

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
