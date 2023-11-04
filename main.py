import os

import cv2
from flask import Flask, request, jsonify

import skew_orient_est
import rotate

app = Flask(__name__)
# Set the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/deskew', methods=['POST'])
def deskew():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Read the uploaded image using OpenCV
        org_image = cv2.imread(filename)

        if org_image is None:
            return jsonify({'error': 'Failed to read the uploaded image'})

    image_name = filename.split("/")[-1]
    image = cv2.cvtColor(org_image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (224, 224))
    orientation = skew_orient_est.orientation_estimate(image)
    orientation_degree_dict = {"down": 180,
                               "left": 90,
                               "right": -90,
                               "up": 0}
    degree = orientation_degree_dict[orientation]
    if degree != 0:
        image = rotate.rotate_image(image, degree)

    skew = skew_orient_est.skew_estimate(image)
    final_skew = degree + (-skew)
    deskewed_image = rotate.rotate_image(org_image, final_skew)
    save_path = os.path.join("/data", image_name)
    cv2.imwrite(save_path, deskewed_image)
    return {"status": "success."}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)
