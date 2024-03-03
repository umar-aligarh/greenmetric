from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    # Receive coordinates from frontend
    coordinates = request.json['coordinates']
    
    # Example: Call a function to generate images and calculate green score using these coordinates
    original_image_url, mask_image_url, green_score = generate_images_and_score(coordinates)
    
    return jsonify({'original_image_url': original_image_url, 'mask_image_url': mask_image_url, 'green_score': green_score})

def generate_images_and_score(coordinates):
    # Add your code to generate images and calculate green score here
    # For demonstration, we'll just return random URLs and score
    original_image_url = "https://example.com/original_image.jpg"
    mask_image_url = "https://example.com/mask_image.jpg"
    green_score = random.randint(50, 100)  # Generate a random score between 50 and 100
    
    return original_image_url, mask_image_url, green_score

if __name__ == '__main__':
    app.run(debug=True)
