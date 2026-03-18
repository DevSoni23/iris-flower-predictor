from flask import Flask

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define a route for the home page
@app.route('/')
def home():
    return "Hello, World! Your app.py is running."

# 3. Run the application locally
if __name__ == '__main__':
    # debug=True allows the server to reload automatically when you save changes
    app.run(debug=True)
