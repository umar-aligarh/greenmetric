from flask import Flask, render_template, request, jsonify
import random
from api import download_img,divide_and_save
app = Flask(__name__)
from mlmodel import prediction
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculatescore', methods=['GET'])
def generatemasks():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},16,0/1024x1024?access_token=" 
    download_img(url)
    divide_and_save("img1024.jpg","static/original")
    green = prediction()
    return render_template('second.html',greenscore=green)

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
