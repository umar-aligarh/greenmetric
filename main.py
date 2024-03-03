# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segment', methods=['POST'])
def segment():
    # Add your forest segmentation code here
    # Example:
    # image = request.files['image']
    # segmented_image = segment_forest(image)
    return "Segmentation completed."

if __name__ == '__main__':
    app.run(debug=True)
