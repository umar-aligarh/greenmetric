from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    # Receive coordinates from frontend
    coordinates = request.json['coordinates']
    
    # Example: Call a function to calculate green score using these coordinates
    green_score = calculate_green_score(coordinates)
    
    return str(green_score)

def calculate_green_score(coordinates):
    # Add your green score calculation logic here
    # Here, we just return a random score as an example
    return random.randint(50, 100)  # Generate a random score between 50 and 100

if __name__ == '__main__':
    app.run(debug=True)
