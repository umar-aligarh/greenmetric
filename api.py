from PIL import Image
import requests

def divide_and_save(image_path, output_path):
    # Open the image
    original_image = Image.open(image_path)

    # Get the size of the image
    width, height = original_image.size

    # Calculate the size of each part
    part_width = width // 4
    part_height = height // 4

    count = 1

    # Loop through each row
    for i in range(4):
        # Loop through each column
        for j in range(4):
            # Define the coordinates of the current part
            left = j * part_width
            upper = i * part_height
            right = (j + 1) * part_width
            lower = (i + 1) * part_height

            # Crop the image to get the current part
            part = original_image.crop((left, upper, right, lower))

            # Save the part as a new image
            part.save(f"{output_path}/part_{count}.jpg")

            count += 1

def download_img(url):
    img_data = requests.get(url).content
    with open('img1024.jpg', 'wb') as handler:
      handler.write(img_data)
# Example usage
input_image_path = "img1024.jpg"
output_directory = "crop"