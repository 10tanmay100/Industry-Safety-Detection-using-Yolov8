from flask import Flask, render_template, request, redirect, send_file, url_for,send_from_directory
from PIL import Image
from ultralytics import YOLO
import os
from io import BytesIO

app = Flask(__name__)
OUTPUT_FOLDER = 'static/detections'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
# Load the model
model = YOLO("best (1).pt")


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            image_bytes = file.read()
            img = Image.open(BytesIO(image_bytes))
            
            results = model(img)  
            filename = 'output_image.jpg'
            file_path = os.path.join(OUTPUT_FOLDER, filename)
            for result in results:
                boxes = result.boxes 
                masks = result.masks  
                keypoints = result.keypoints  
                probs = result.probs 
                result.save(file_path) 

            return redirect(url_for('display_image', filename=filename))
    return render_template('upload.html')

@app.route('/display/<filename>')
def display_image(filename):
    # Serve the processed image
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
