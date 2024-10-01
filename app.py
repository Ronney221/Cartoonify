from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from PIL import Image
import os
import time
import torch
from model import load_model, preprocess_image, apply_style_transfer
from torchvision import transforms

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['GENERATED_FOLDER'] = 'static/avatars/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['GENERATED_FOLDER']):
    os.makedirs(app.config['GENERATED_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        generated_images = os.listdir(app.config['GENERATED_FOLDER'])
        return render_template('index.html', generated_images=generated_images)

    if request.method == 'POST':
        style = request.form.get('style')
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        # Open the image using PIL
        image = Image.open(file.stream)

        # Convert the image to RGB if it's in RGBA mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Save the cropped image
        original_filename = f"cropped_{int(time.time())}.jpg"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        image.save(file_path)

        # Preprocess image and load the model
        image_tensor = preprocess_image(image)
        model = load_model(style)

        # Apply CycleGAN model for style transfer
        stylized_image_tensor = apply_style_transfer(image_tensor, model)

        # Denormalize the image tensor
        stylized_image_tensor = denormalize(stylized_image_tensor)

        # Convert the output tensor back to a PIL image
        stylized_image = transforms.ToPILImage()(stylized_image_tensor.squeeze(0))

        # Save the stylized image
        avatar_filename = f"styled_{original_filename}"
        avatar_path = os.path.join(app.config['GENERATED_FOLDER'], avatar_filename)
        stylized_image.save(avatar_path)

        # Return the filename in JSON format
        return jsonify({'avatar_filename': avatar_filename})

@app.route('/avatar/<avatar_filename>')
def show_avatar(avatar_filename):
    avatar_url = url_for('static', filename='avatars/' + avatar_filename)
    return render_template('avatar.html', avatar_url=avatar_url, avatar_filename=avatar_filename)

@app.route('/download/<avatar_filename>')
def download_image(avatar_filename):
    file_path = os.path.join(app.config['GENERATED_FOLDER'], avatar_filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
