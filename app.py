from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    return "<h1>Hello, World! This is my first Python Web App!</h1>"

# Run the application if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
